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
    email = Column(String, nullable=False)
    phone = Column(BigInteger, nullable=False)
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



class Shipper(Base):
    __tablename__ = "t_shipper"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))
    name = Column(String, nullable=False)
    logo = Column(String, nullable=False)
    corporate_address = Column(String, nullable=False)
    billing_address = Column(String, nullable = False)
    contact_name = Column(String, nullable = False)
    contact_no = Column(BigInteger, nullable = False)
    email = Column(String, nullable = False)
    pan = Column(String, nullable = False)
    tan = Column(String, nullable = False)
    gst_in = Column(String, nullable = False)
    cin_no = Column(BigInteger, nullable = False)
    cin = Column(String, nullable = False)
    inc_cert = Column(String, nullable = False)
    trade_lic = Column(String, nullable = False)
    has_regions = Column(Boolean, default = False, nullable = False)
    has_branches = Column(Boolean, default = False, nullable = False)
    status = Column(Enum('approved', 'pending', 'rejected', name = 'approval_status'), default = 'pending')
    is_active = Column(Boolean, default = False, nullable = False)
    created_at = Column(DateTime, nullable = False, server_default = text("now()"))
    created_by = Column(UUID(as_uuid=True),  nullable = False)
    updated_at = Column(DateTime, nullable = True)
    updated_by = Column(UUID(as_uuid=True), nullable = True)   