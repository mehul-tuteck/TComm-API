from dotenv import load_dotenv
from fastapi import FastAPI

from routes import routes

load_dotenv()


app = FastAPI()

routes.Routes(app)

