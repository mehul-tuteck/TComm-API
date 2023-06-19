from pydantic import BaseModel,EmailStr,constr

class UserIn(BaseModel):
    first_name : str
    last_name : str
    email : EmailStr | None = None
    phone : constr(strip_whitespace=True) | None = None
    password : constr(min_length=8, strip_whitespace=True) 
    age : int | None = None
    gender : str | None = None
    address : constr(strip_whitespace=True) | None = None
    
    class Config:
        orm_mode = True


