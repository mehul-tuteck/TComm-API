from dotenv import load_dotenv;
load_dotenv();

from fastapi import FastAPI;

from routers import routes;

from utils import queries_user 



app = FastAPI()

routes.Routes(app)

#call the method while generating new table in db using sqlalchemy ORM

try:
 queries_user.generate_tb();
except Exception as ex:
     print(str(ex)); 









