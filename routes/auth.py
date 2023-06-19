from fastapi import APIRouter
from controllers.auth import Register, GetOTP, VerifyOTP, Login, ForgotPassword, ResetPassword, Logout

router = APIRouter(prefix="/api/v1")

@router.post("/register")
async def register():
    return await Register()

@router.get("/OTP")
async def get_otp():
    return await GetOTP()

@router.post("/OTP/verify")
async def verify_otp():
    return await VerifyOTP()

@router.post("/login")
async def login():
    return await Login()

@router.post("/password/forgot")
async def forgot_password():
    return await ForgotPassword()

@router.post("/password/reset")
async def reset_password():
    return await ResetPassword()

@router.post("/logout")
async def logout():
    return await Logout()
