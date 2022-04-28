from typing import Optional
from pydantic import BaseModel, Field


class insert_paye(BaseModel):
    name: str = Field(default=None, description='the name of paye')
    manager_code: str = Field(default=None, description='the manager_code')
    school_code: str = Field(default=None, description='the school_code')


class paye_list(BaseModel):
    manager_code: str = Field(default=None, description='the manager_code')


class delete_paye(BaseModel):
    manager_code: str = Field(default=None, description='the manager_code')
    paye_code: str = Field(default=None, description='the paye_code')