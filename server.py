from fastapi import FastAPI;
from dotenv import load_dotenv;
load_dotenv()
from routers import mount_routes;
from utils import queries_user;

from fastapi.middleware.cors import CORSMiddleware;
from middleware.auth import auth_middleware

from config.db import Base, engine

app = FastAPI()

mount_routes.Routes(app)

#call the method while generating new table in db using sqlalchemy ORM
"""
try:
 queries.generate_tb();
except Exception as ex:
     print(str(ex)); 
"""








