from pydantic import BaseModel, Field
from typing import Optional


class insert_student(BaseModel):
    manager_code: str = Field(default=None)
    school_code: str = Field(default=None)
    name: str = Field(default=None)
    family: str = Field(default=None)
    age: Optional[int]
    description: Optional[str]
    Gender: bool = Field(default=True)
    paye_token :str =Field(default=None)
    paye_name:str = Field(default=None)



class  get_list_student(BaseModel):
    manager_code: str = Field(default=None)
    school_code: str = Field(default=None)


class delete_student(BaseModel):
    manager_code: str = Field(default=None)
    school_code: str = Field(default=None)
    student_token:str = Field(default=None)


class update_student(BaseModel):
    name: Optional[str]
    family: Optional[str]
    age: Optional[int]
    description: Optional[str]
    Gender: Optional[bool]
    student_token:str = Field(default=None , description='the student token ')


