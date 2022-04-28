from pydantic import BaseModel, Field
from typing import Optional


class addSchool(BaseModel):
    name: str = Field(default=None, max_length=80, description='the name of school ')
    kind: bool = Field(default=True, description='the boy ==True')
    paye: str = Field(default=None, description='witch paye highschool or lower ')
    address: Optional[str] = None
    manager_code: str = Field(default=None, description='the user token')


class delete_school(BaseModel):
    manager_code: str = Field(default=None, description='the user token')
    school_code: str = Field(default=None, description='the school token')


class school_list(BaseModel):
    manager_code: Optional[str] = Field(default=None, description='the user token')

