from fastapi import FastAPI
from routes import routes

app = FastAPI()

routes.Routes(app)

@app.get("/check")
async def check():
    return {"Hello" : "World!"}