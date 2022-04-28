from pydantic import BaseModel, Field
from typing import Optional


class input_login(BaseModel):
    username: str = Field(default=None, description="the username")
    passwords: str = Field(default=None, description="the passwords")



class create_user(BaseModel):
    name:str=Field(default=None )
    phone: str = Field(default=None)
    email: Optional[str]
    username: str = Field(default=None)
    passwords:str=Field(default=None)


class send_SMS(BaseModel):
   phone:str=Field(default=None , description='the phone user phone')


class token(BaseModel):
    phone:str=Field(default=None , description='the mobile of user')

