from sqlalchemy import BigInteger, Boolean, Column, DateTime, Enum, ForeignKey, Integer, String, text
from sqlalchemy.dialects.postgresql import UUID

from config.db import Base

#gen_random_uuid()
#uuid_generate_v4()

class User(Base):
    __tablename__ = "t_users"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(BigInteger)
    password = Column(String,nullable = False)
    address = Column(String)
    age = Column(Integer)
    gender = Column(String)
    is_active = Column(Boolean,default = False,nullable = False)
    created_by = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))
    updated_by = Column(String)
    updated_at = Column(DateTime)



   
class UserCache(Base):
    __tablename__ = "t_user_cache"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(BigInteger)
    password = Column(String, nullable = False)
    otp = Column(BigInteger, nullable = True)
    address = Column(String)
    age = Column(Integer)
    gender = Column(String)
    is_active = Column(Boolean,default = False,nullable = False)
    created_by = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))
    updated_by = Column(String)
    updated_at = Column(DateTime)