from fastapi import Request;
from starlette.middleware.base import BaseHTTPMiddleware;
from jose import JWTError, jwt;
import os;

class auth_middleware(BaseHTTPMiddleware):
  async def dispatch(self, request : Request, call_next):
    #print(request.headers.get("authorization"));
    if request.url.path == "/authorization_authentication/password/reset":
      authorized_token:str = request.headers.get("authorization");
      token = authorized_token.split(" ")[1];
      decoded_jwt = jwt.decode(token, os.getenv("JWT_SECRET_KEY"), algorithms= os.getenv("JWT_ALGORITHM"));
      request.state.user_id = decoded_jwt.get("userId");
      response = await call_next(request)
     # print(request)
      #print(response)
      return response
    else:
      return await call_next(request);

      
      
  
 