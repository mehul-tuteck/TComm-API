import re

async def get_user_by_id():
    return 

async def get_user_by_credentials(ph : str, email : str):
    return

async def validate_password(password : str):
    
    pattern = (
    r"^(?=.*[A-Z])"  # At least one uppercase letter
    r"(?=.*[a-z])"   # At least one lowercase letter
    r"(?=.*\d)"      # At least one numeric digit
    r"(?=.*[!@#$%^&*()-=_+{};':\"\\|,.<>/?])"  # At least one special character
    r".{8,}$"        # Minimum length of 8 characters
)
    if not re.match(pattern=pattern,string=password):
        return False
    return True