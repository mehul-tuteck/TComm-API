from fastapi import APIRouter, Response, Header;
from email_validator import validate_email,EmailNotValidError

from models.User import User as UserModel;
from schemas.userDTO import UserIn
from utils.response import SuccessResponse,ErrorResponse,ServerError,NotFoundError
from utils.user import validate_password,get_user_by_credentials,create_new_user
from utils.queries import fetch_user, fetch_user_with_id, set_new_password
from config.db import Session
from utils.token_handler import create_access_token;
from starlette.requests import Request;




router = APIRouter(prefix="/authorization_authentication")



@router.post("/register")
async def register(user : UserIn):
    try:
      
        if not (user.email and user.phone):
            return ErrorResponse(data=None,client_msg="Your E-mail ID or phone is incorrect/Not entered!",dev_msg="Email/Phone field is empty")
      
        if not validate_email(email=user.email):
            return ErrorResponse(data=EmailNotValidError,client_msg="Your E-mail ID is invalid!",dev_msg="Email validation did not pass")
      
        if not validate_password(password=user.password):
            return ErrorResponse(data=None,client_msg="Your E-mail ID is invalid!",dev_msg="Email validation did not pass")
    
        if get_user_by_credentials(ph=user.phone, email=user.email):
            return ErrorResponse(data=None,client_msg="A user with the same phone number/email ID already exists!",dev_msg="User already exists!")

        new_user = create_new_user(user=user)
        

        
        return SuccessResponse(data=None,client_msg="You are successfully registered!",dev_msg="Registration Successful!")
    
    except Exception as e:

        return ServerError(err=e,errMsg=str(e))



@router.get("/OTP")
async def get_otp():
    try:
        return SuccessResponse(data=None,client_msg="You are successfully registered!",dev_msg="Registration Successful!")
    
    except Exception as e:
        return ServerError(err=e,errMsg=str(e))
   

@router.post("/OTP")
async def verify_otp():
    try:
        return SuccessResponse(data=None,client_msg="You are successfully registered!",dev_msg="Registration Successful!")
    
    except Exception as e:
        return ServerError(err=e,errMsg=str(e))
    
@router.post("/OTP/resend")
async def resend_otp():
    try:
        return SuccessResponse(data=None,client_msg="You are successfully registered!",dev_msg="Registration Successful!")
    
    except Exception as e:
        return ServerError(err=e,errMsg=str(e))


@router.post("/login")
async def login(requestedUser: UserIn):
    
    try:

        userObjFromDB = fetch_user(inputEmail = requestedUser.email, inputPhone = requestedUser.phone)
    
        if userObjFromDB:
            if userObjFromDB[0].password == requestedUser.password :
               token = create_access_token(userDetails = userObjFromDB[0]);
               return SuccessResponse(data=token, client_msg="You are successfully logged in!", dev_msg="LogIn Successful!")
            else:
                return ErrorResponse(client_msg="Password did not match!", dev_msg="Password missmatched!");
        else:
            return ErrorResponse(client_msg="User not found with given credential", dev_msg="User not found with given credential!")
    
    except Exception as e:
        return ServerError(err=e,errMsg=str(e))
 

@router.post("/password/forgot")
async def forgot_password():
    try:
        return SuccessResponse(data=None,client_msg="You are successfully registered!",dev_msg="Registration Successful!")
    
    except Exception as e:
        return ServerError(err=e,errMsg=str(e))
    

@router.patch("/password/reset")
async def reset_password(request: Request):
    try:
        user_id = request.state.user_id;
        request_body_data = await request.json();
        new_password = request_body_data.get("new_password");
       
        if user_id and new_password:
            user = fetch_user_with_id(user_id);
            if user:
                set_new_password(user_id, new_password);
            else:
                return ErrorResponse(client_msg= "User not exists!", dev_msg= "User not exists with given user id!");
        else:
            return ErrorResponse(client_msg="Please logged in to reset your password!", dev_msg="Fetch user id from token and new_password from request body!");
        
        return SuccessResponse(data=user_id,client_msg="You are successfully registered!", dev_msg="Registration Successful!")
    
    except Exception as e:
        return ServerError(err=e,errMsg=str(e))


@router.post("/logout")
async def logout():
    try:
        return SuccessResponse(data=None,client_msg="You are successfully registered!",dev_msg="Registration Successful!")
    
    except Exception as e:
        return ServerError(err=e,errMsg=str(e))
   
   