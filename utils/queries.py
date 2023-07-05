from config.db import Base, engine, Session, session
from sqlalchemy import select, or_, update
from models.User import User as UserModel
def generate_tb():
   Base.metadata.create_all(engine)


def fetch_user(inputEmail: str, inputPhone: int):
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
   
    
"""
def insert_tb():
       with Session(engine) as session:


    id = Column(UUID, primary_key=True, server_default=text("gen_random_uuid()"))
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(BigInteger)
    password = Column(String,nullable = False)
    address = Column(String)
    age = Column(Integer)
    gender = Column(String)
    is_active = Column(Boolean,default = False,nullable = False)
    created_by = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))
    updated_by = Column(String)
    updated_at = Column(DateTime)
"""    