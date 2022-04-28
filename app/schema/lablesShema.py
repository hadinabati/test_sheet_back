from typing import Optional
from pydantic import Field, BaseModel


class insert_Lable(BaseModel):
    name: str = Field(default=None, description='the name of lable')
    manager_code: str = Field(default=None)
    student_info: list


class delete_lable(BaseModel):
    token:str =Field(default=None)
    manager_code:str = Field(default=None)

class lables_list(BaseModel):
    manager_code:str = Field(default=None)
