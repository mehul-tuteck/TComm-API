from passlib.context import CryptContext;
import random


def generate_hash_password(password : str):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto");
    hash_password = pwd_context.hash(password);
    print(hash_password);

    return hash_password;


def generate_otp():
    return random.randint(1000, 9999);
    
    