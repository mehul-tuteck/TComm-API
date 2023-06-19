from .auth import router as auth

def Routes(app):
    app.include_router(auth)