import re

from models.User import User as UserModel
from schemas.userDTO import UserIn
from utils.security_utils import generate_hash_password;

async def create_new_user(user : UserIn) -> UserModel :
      print("hash_pwd")
      print(hash_pwd)
      print(user.password)

      return UserModel(
        first_name = user.first_name,
        last_name = user.last_name,
        email = user.email,
        phone = user.phone,
        password = user.password,
        address = user.address,
        age = user.age,
        gender = user.gender,
        is_active = False
    )
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