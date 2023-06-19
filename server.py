
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI

from routes import routes


app = FastAPI()
routes.Routes(app)

