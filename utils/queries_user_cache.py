from config.db import Base, engine, Session, session;

from sqlalchemy import select, or_, update;


from models.User import UserCache;
from schemas.userDTO import UserIn;
from utils.security_utils import generate_hash_password;

import uuid;
from datetime import datetime;

def insert_user_cache(userDetails : UserIn):
    
    new_user_cache = UserCache(
        
         id = str(uuid.uuid4()),
         first_name = userDetails.first_name,
         last_name = userDetails.last_name,
         email = userDetails.email,
         phone = userDetails.phone,
         password = generate_hash_password(userDetails.password),
         otp = userDetails.otp,
         address = userDetails.address,
         age = userDetails.age,
         gender = userDetails.gender,
         is_active = False,
         created_by = "Admin",
         updated_by = None,
         created_at = datetime.now(),
         updated_at = None
        
    );
    session.add(new_user_cache);
    session.commit();



def fetch_cache_user_by_email_or_phone(inputEmail: str, inputPhone: int):

   fetchedUserQuery = select(UserCache).where(
        (UserCache.email == inputEmail) |
        (UserCache.phone == inputPhone)
   );
   fetchedUser = session.execute(fetchedUserQuery).fetchone()
   return fetchedUser;
    
def fetch_cache_user_with_id(id : str):
    query = select(UserCache).where(
        UserCache.id == id
    );
    cache_user = session.execute(query).fetchone();
    return cache_user;