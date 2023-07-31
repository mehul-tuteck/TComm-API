from fastapi import APIRouter, Response, Header, Depends;
from email_validator import validate_email, EmailNotValidError
from fastapi.security import OAuth2PasswordBearer;

from models.User import User as UserModel;
from schemas.userDTO import UserIn, ResGenerateOTP, UserToBeInsert
from utils.security_utils import generate_random_otp, send_otp_in_email, send_otp_in_phone;

from utils.response import SuccessResponse,ErrorResponse,ServerError,NotFoundError
from utils.user import validate_password,get_user_by_credentials,create_new_user
from utils.queries_user import fetch_user_by_email_or_phone, fetch_user_with_id, set_new_password, insert_user, delete_with_email
from utils.queries_user_cache import insert_user_cache, fetch_cache_user_by_email_or_phone, fetch_cache_user_with_id, update_with_otp
from config.db import Session
from utils.token_handler import create_access_token, decode_token, encode_token, modified_exp;
from models.User import UserCache;

from starlette.requests import Request;
from datetime import datetime, timedelta;

import random



router = APIRouter(prefix="/api/auth")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl= '/login');

@router.post("/register")
async def register(userDetails : UserIn):
    try:

        if not (userDetails.email and userDetails.phone):
            return ErrorResponse(data = None, client_msg = "Your E-mail ID or phone is incorrect/Not entered!", dev_msg = "Email/Phone field is empty");
        if not validate_email(email = userDetails.email):
            return ErrorResponse(data = EmailNotValidError, client_msg = "Your E-mail ID is invalid!", dev_msg = "Email validation did not pass");
        if not userDetails.password:
            return ErrorResponse(data = None, client_msg = "Please provide a valid password!", dev_msg = "Password missing from client side!");
        if not validate_password(password = userDetails.password):
           return ErrorResponse(data = None, client_msg = "Your E-mail ID is invalid!", dev_msg = "Email validation did not pass");
    
        new_user = fetch_cache_user_by_email_or_phone(inputEmail = userDetails.email, inputPhone = userDetails.phone);
   
        if new_user:
            return ErrorResponse(data = None, client_msg = "Please, retry to register!", dev_msg = "User details not inserted into cache table.");

        insert_user_cache(userDetails);
        
        return SuccessResponse(data = new_user[0], client_msg = "Information are collected.", dev_msg = "Informations are inserted into cache, next step verify otp");

    except Exception as e:

        return ServerError(err = e, errMsg = str(e));
    

@router.post("/OTP/generate")
async def get_otp(userDetails : UserIn):
    try:
        if not userDetails.id :
            return ErrorResponse(data = None, client_msg = "Enter details to get otp.", dev_msg = "collected user id from cache table.");
        
        cache_user = fetch_cache_user_with_id(id = userDetails.id);

        if not cache_user :
            return ErrorResponse(data = None, client_msg = "Enter details to get otp.", dev_msg = "collected user id from cache table.");
    
        userDetails.otp = generate_random_otp();
        update_with_otp(userDetails = userDetails);
        
        if userDetails.email:
            send_otp_in_email(otp = userDetails.otp, email = userDetails.email);

        if userDetails.phone:    
            send_otp_in_phone(phone = userDetails.phone, otp = userDetails.otp);
        
        print("The otp is", userDetails.otp);
        
        resGenerateOTP = ResGenerateOTP();

        return SuccessResponse(data = userDetails.id  ,client_msg="You are successfully registered!",dev_msg="Registration Successful!")
    
    except Exception as e:
        return ServerError(err=e,errMsg=str(e))
   

@router.post("/OTP/verify")
async def verify_otp(userDetails : UserIn):
    try:

        if not userDetails.id :
            return ErrorResponse(data = None, client_msg = "Enter your details", dev_msg = "collect user id from cache");
        if not userDetails.otp :
            return ErrorResponse(data = None, client_msg = "Enter the otp.", dev_msg = "Collect the otp from user");
    
        cache_user = fetch_cache_user_with_id(id = userDetails.id);
        
        if not cache_user :
            return ErrorResponse(data = None, client_msg = "Enter your details", dev_msg = "collect user id from cache");
        
        
        if not (cache_user[0].otp == userDetails.otp) :
          return ErrorResponse(data = None, client_msg = "OTP didn't match!", dev_msg = "OTP didn't match!");
       
        user_to_be_inserted = UserToBeInsert();
        user_to_be_inserted.id = cache_user[0].id;
        user_to_be_inserted.first_name = cache_user[0].first_name;
        user_to_be_inserted.last_name = cache_user[0].last_name;
        user_to_be_inserted.email = cache_user[0].email;
        user_to_be_inserted.phone = cache_user[0].phone;
        user_to_be_inserted.password = cache_user[0].password;
        user_to_be_inserted.address = cache_user[0].address;
        user_to_be_inserted.age = cache_user[0].age;
        user_to_be_inserted.gender = cache_user[0].gender;
        

        new_user = insert_user( user_to_be_inserted);  

        print("After Insertion->1");
        get_new_user = fetch_user_by_email_or_phone(user_to_be_inserted.email, None);

        print("After Insertion", get_new_user[0]);
        if not get_new_user :
           return ErrorResponse(data = None, client_msg = "You have to enter your details to register!", dev_msg = "Register process is interrupted, check code and user data");
        delete_with_email(user_to_be_inserted.email, UserCache);
        return SuccessResponse(data = get_new_user[0], client_msg="You are successfully registered!", dev_msg="Registration Successful!")
    
    except Exception as e:
        return ServerError(err=e, errMsg=str(e))
    
@router.post("/OTP/resend")
async def resend_otp():
    try:
        return SuccessResponse(data=None,client_msg="You are successfully registered!",dev_msg="Registration Successful!")
    
    except Exception as e:
        return ServerError(err=e,errMsg=str(e))


@router.post("/login")
async def login(requestedUser: UserIn):
    
    try:

        userObjFromDB = fetch_user_by_email_or_phone(inputEmail = requestedUser.email, inputPhone = requestedUser.phone);
    
        if not userObjFromDB:
            return ErrorResponse(client_msg = "User not found with given credential!", dev_msg = "User not found with given credential!");
    
        if userObjFromDB[0].password != requestedUser.password :
            return ErrorResponse(data=[], client_msg = "Password did not match!", dev_msg = "Password missmatched!"); 
      
        token = create_access_token(userDetails = userObjFromDB[0]);

        return SuccessResponse(data = token, client_msg = "You are successfully logged in", dev_msg = "LogIn Successful");
    
    except Exception as e:
        return ServerError(err = e, errMsg = str(e))
 

@router.patch("/password/forgotten")
async def forgotten_password(request_body : UserIn):
    try:

        if not (request_body.email or request_body.phone):
            return ErrorResponse(client_msg = "Email or phone number required to identify user.", dev_msg = "Email or phone number required to identify user.");
    
        user = fetch_user_by_email_or_phone(request_body.email, request_body.phone);

        if not user:
            return ErrorResponse(client_msg = "User not found!", dev_msg = "User not present with provided identifier!");
    
        if not request_body.password :
            return ErrorResponse(client_msg = "Please enter a new password to set.", dev_msg = "Please enter a new password to set."); 
    
        changed_password =  set_new_password(user[0].id, request_body.password);
        #user_new = UserIn();
        #user_new = user[0];
        
        return SuccessResponse(data = changed_password, client_msg="Password changed successfully!", dev_msg="Password changed successfully!");

    except Exception as e:
        return ServerError(err=e,errMsg=str(e))
    

@router.patch("/password/reset")
async def reset_password(request: Request, userIn: UserIn):

    try:

        user_id = request.state.user_id;
        
        #request_body_data = await request.json();
        #new_password = request_body_data.get("password");
        new_password = userIn.password;
       
        if not user_id and new_password:
            return ErrorResponse(data = [], client_msg = "Please enter the password !", dev_msg = "Fetch user id from token and new_password from request body!");
    
        user = fetch_user_with_id(user_id);

        if not user:
            return ErrorResponse(data = [], client_msg= "User not exists!", dev_msg= "User not exists with given user id!");
    
        reset_password = set_new_password(user_id, new_password);
            
        return SuccessResponse(data = reset_password, client_msg = "Password successfully setted.", dev_msg = "Passward successfully re-setted with new password");
    
    except ValueError as ve:
        return ErrorResponse(client_msg = "Invalid request data!", dev_msg = str(ve));
    
    except Exception as e:
        return ServerError(err = e, errMsg = str(e));


@router.post("/logout")
async def logout(auth_token : str = Depends(oauth2_scheme)):
    try:

        decoded_token = decode_token(auth_token);
        decoded_token['exp'] = datetime.utcnow() + timedelta(milliseconds = 1);
        new_token = encode_token(decoded_token);
        new_auth_token = 'Bearer '+new_token;

        return SuccessResponse(data = new_auth_token, client_msg = "You have successfully logged out.", dev_msg = "User logged out.");

    except Exception as e:

        return ServerError(err=e,errMsg=str(e))
   
   