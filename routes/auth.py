from fastapi import APIRouter,Response
from email_validator import validate_email,EmailNotValidError


from Types.user import User
from utils.response import SuccessResponse,ErrorResponse,ServerError,NotFoundError
from utils.user import validate_password,get_user_by_credentials


router = APIRouter(prefix="/api/v1")

@router.post("/register")
async def register(user : User):
    try:
      
        if not (user.email and user.phone):
            return ErrorResponse(data=None,client_msg="Your E-mail ID or phone is incorrect/Not entered!",dev_msg="Email/Phone field is empty")
      
        if not validate_email(email=user.email):
            return ErrorResponse(data=EmailNotValidError,client_msg="Your E-mail ID is invalid!",dev_msg="Email validation did not pass")
      
        if not validate_password(password=user.password):
            return ErrorResponse(data=None,client_msg="Your E-mail ID is invalid!",dev_msg="Email validation did not pass")
    
        if get_user_by_credentials(ph=user.phone, email=user.email):
            return ErrorResponse(data=None,client_msg="A user with the same phone number/email ID already exists!",dev_msg="User already exists!")


 
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
async def login():
    try:
        return SuccessResponse(data=None,client_msg="You are successfully registered!",dev_msg="Registration Successful!")
    
    except Exception as e:
        return ServerError(err=e,errMsg=str(e))
 

@router.post("/password/forgot")
async def forgot_password():
    try:
        return SuccessResponse(data=None,client_msg="You are successfully registered!",dev_msg="Registration Successful!")
    
    except Exception as e:
        return ServerError(err=e,errMsg=str(e))
    

@router.post("/password/reset")
async def reset_password():
    try:
        return SuccessResponse(data=None,client_msg="You are successfully registered!",dev_msg="Registration Successful!")
    
    except Exception as e:
        return ServerError(err=e,errMsg=str(e))


@router.post("/logout")
async def logout():
    try:
        return SuccessResponse(data=None,client_msg="You are successfully registered!",dev_msg="Registration Successful!")
    
    except Exception as e:
        return ServerError(err=e,errMsg=str(e))
   