
from dotenv import load_dotenv
#from models import User
load_dotenv()

from utils import queries

from fastapi import FastAPI

from routes import routes


app = FastAPI()
routes.Routes(app)


#queries.generate_tb()







