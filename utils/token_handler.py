#import libraries
from models.User import User as UserModel;
from datetime import datetime, timedelta;
from jose import JWTError, jwt;
from utils.response import SuccessResponse,ErrorResponse,ServerError,NotFoundError

SECRET_KEY = "09d25e094faaPythonTCOMM-APISecretf7099f6f0f4caa6cf63b88e8d3e7";
#SECRET_KEY = "PythonTCOMM-APISecret";
ALGORITHM = "HS256";
AUTHORIZED_KEY = "Bearer ";


def create_access_token(userDetails : UserModel):
     try:
          expiration_time = datetime.utcnow() + timedelta(hours = 1);
          #print(userDetails.first_name+userDetails.email);
          claims = {
               'userId' : str(userDetails.id),
               'exp' : expiration_time
          } ;
       
          encoded_jwt = jwt.encode(claims, SECRET_KEY, algorithm=ALGORITHM);
          return AUTHORIZED_KEY+encoded_jwt;
     except Exception as e:
          return ErrorResponse(data=[], client_msg="error in token generation!", dev_msg=str(e));
         

            
        #  to_encode.update({"exp": expire});
