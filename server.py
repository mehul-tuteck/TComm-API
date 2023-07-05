from fastapi import FastAPI;
from dotenv import load_dotenv;
load_dotenv()
from routers import mount_routes;
from utils import queries;

from fastapi.middleware.cors import CORSMiddleware;
from middleware.auth import auth_middleware

app = FastAPI()

mount_routes.Routes(app)

#call the method while generating new table in db using sqlalchemy ORM


#queries.generate_tb()







