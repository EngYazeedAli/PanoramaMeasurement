from pydantic import BaseModel, validator
from typing import Optional
import bcrypt
salt_rounds = 12

class User(BaseModel):

    name: str
    email: str
    password: str
    role: Optional[str] = "USER"
    is_active: Optional[bool] = False
    

    @validator("password")
    def hash_password(cls, value):
        return bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt(salt_rounds)).decode('utf-8')
    
    @validator("email")
    def convert_email_to_lowercase(cls, value):
        return value.lower()

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Yazeed",
                "email": "Yazeed@gmail.com",
                "password": "yazeed@12"
            }
        }

class UpdateUser(BaseModel):

    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    
    @validator("password")
    def hash_password(cls, value):
        return bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt(salt_rounds)).decode('utf-8')
    
    @validator("email")
    def convert_email_to_lowercase(cls, value):
        return value.lower()

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Yazeed",
                "email": "Yazeed@gmail.com",
                "password": "yazeed@12"
            }
        }

class Login(BaseModel):
    
    email: str
    password: str

    @validator("email")
    def convert_email_to_lowercase(cls, value):
        return value.lower()


    class Config:
        json_schema_extra = {
            "example": {
                "email": "Yazeed@gmail.com",
                "password": "yazeed@12"
            }
        }