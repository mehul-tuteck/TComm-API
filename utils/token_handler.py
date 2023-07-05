from dotenv import load_dotenv;
load_dotenv()

#import libraries
from models.User import User as UserModel;
from datetime import datetime, timedelta;
from jose import JWTError, jwt;
from utils.response import SuccessResponse,ErrorResponse,ServerError,NotFoundError

import os


def create_access_token(userDetails : UserModel):
     try:
          expiration_time = datetime.utcnow() + timedelta(hours = 1);
          print(userDetails.first_name+" "+userDetails.email);
          claims = {
               'userId' : str(userDetails.id),
               'exp' : expiration_time
          } ;
          #print(os.environ);
          encoded_jwt = jwt.encode(claims, os.getenv("JWT_SECRET_KEY"), algorithm=os.getenv("JWT_ALGORITHM"));
          return os.getenv("JWT_AUTHORIZED_KEY")+" "+encoded_jwt;
     except Exception as e:
          return ErrorResponse(data=[], client_msg="error in token generation!", dev_msg=str(e));
         

            
        #  to_encode.update({"exp": expire});
