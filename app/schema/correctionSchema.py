from pydantic import  BaseModel , Field
from typing import  Optional


class Upload(BaseModel):
    Azmoon_token:str =Field(default=None , description='the azmoon token')
    file_info: list = Field(default={"path" : '' , 'student_token':''}, description='the azmoon info')