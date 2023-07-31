from config.db import Base, engine, Session, session;

from sqlalchemy import select, or_, update, delete;

from models.User import User as UserModel;
from models.User import UserCache;
from schemas.userDTO import UserIn;
from utils.security_utils import generate_hash_password;

import uuid;
from datetime import datetime;


def generate_tb():
   Base.metadata.create_all(engine)


def fetch_user_by_email_or_phone(inputEmail: str, inputPhone: int):

   fetchedUserQuery = select(UserModel).where(
        (UserModel.email == inputEmail) |
        (UserModel.phone == inputPhone)
   );
   fetchedUser = session.execute(fetchedUserQuery).fetchone()
   return fetchedUser

def fetch_user_with_id(id : str):
    query = select(UserModel).where(
       (UserModel.id == id)
    );
    user = session.execute(query).fetchone();
    return user;


def set_new_password(id: str, new_password: str):
   try:
      query = update(UserModel).where(
         UserModel.id == id
      ).values(
         password = new_password 
         );
      change_password = session.execute(query);
      session.commit(); #commit the changes into database
      return change_password;
   except Exception as e :
      print(str(e));
   
def insert_user(userDetails : UserIn):
       
      new_user = UserModel(
         id = str(uuid.uuid4()),
         first_name = userDetails.first_name,
         last_name = userDetails.last_name,
         email = userDetails.email,
         phone = userDetails.phone,
         password = generate_hash_password(userDetails.password),
         address = userDetails.address,
         age = userDetails.age,
         gender = userDetails.gender,
         is_active = False,
         created_by = "Admin",
         updated_by = None,
         created_at = datetime.now(),
         updated_at = None
      );
      session.add(new_user);
      session.commit();
      #return inserted_record;


def delete_with_email(inputEmail : str, modelClass : any):
   stmt = delete( modelClass ).where( modelClass.email == inputEmail );
   session.execute(stmt);
   session.commit();
               





