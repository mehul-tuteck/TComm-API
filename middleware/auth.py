from fastapi import Request;
from starlette.middleware.base import BaseHTTPMiddleware;

from utils.response import ServerError;

from jose import JWTError, jwt;
import os;

class auth_middleware(BaseHTTPMiddleware):
  async def dispatch(self, request : Request, call_next):
    try:

      if request.url.path == "/api/auth/password/reset":
        authorized_token:str = request.headers.get("authorization");
        token = authorized_token.split(" ")[1];
        try:
          decoded_jwt = jwt.decode(token, os.getenv("JWT_SECRET_KEY"), algorithms = os.getenv("JWT_ALGORITHM"));
        except Exception as ex:
           return ServerError(err = ex, errMsg = str(ex));

        request.state.user_id = decoded_jwt.get("userId");
        
        response = await call_next(request);
        
        return response
      
      else:
        return await call_next(request);
  
    except Exception as ex:
      return ServerError(err = ex, errMsg = str(ex));
 

      
      
  
 