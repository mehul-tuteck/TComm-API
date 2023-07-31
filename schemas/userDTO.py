from pydantic import BaseModel,EmailStr,constr

class UserIn(BaseModel):
    #password_pattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"

    id : str | None = None
    first_name : str | None = None 
    last_name : str  | None = None
    email : EmailStr | None = None
    phone : constr(strip_whitespace=True) | None = None
    password : constr(min_length=8, strip_whitespace=True) | None = None #regex = password_pattern) 
    otp : int | None = None
    age : int | None = None
    gender : str | None = None
    address : constr(strip_whitespace=True) | None = None

    class Config:
        orm_mode = True




class UserToBeInsert(BaseModel):
    #password_pattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"

    id : str | None = None
    first_name : str | None = None 
    last_name : str  | None = None
    email : EmailStr | None = None
    phone : constr(strip_whitespace=True) | None = None
    password : constr(min_length=8, strip_whitespace=True) | None = None #regex = password_pattern) 
    age : int | None = None
    gender : str | None = None
    address : constr(strip_whitespace=True) | None = None

    class Config:
        orm_mode = True       



class ResGenerateOTP(BaseModel):
    id : str | None = None
    otp : int | None = None     


        


    

