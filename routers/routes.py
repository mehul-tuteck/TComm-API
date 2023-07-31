
from routers.auth import router as auth_router
from middleware.auth import auth_middleware


def Routes(app):

    #adding the middleware within app
    app.add_middleware(auth_middleware)
    
    #mounting the route within app
    app.include_router(auth_router); 
   

    