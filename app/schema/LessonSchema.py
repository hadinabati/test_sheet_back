from typing import Optional
from pydantic import Field, BaseModel


class lesson_create(BaseModel):
    name: str = Field(default=None, description='the name of lesson')
    kind: bool = Field(default=True, description='if it is public it is True')
    school_token: str = Field(default=None, description='the school token')
    manager_token: str = Field(default=None, description='the manager_token')
    description: Optional[str]


class lesson_delete(BaseModel):
    token: str = Field(default=None, description='the token of lesson')
    manager_token: str = Field(default=None, description='the manager_token')

class all_lesson(BaseModel):
    manager_token: str = Field(default=None, description='the manager_token')
    school_token: str = Field(default=None, description='the school_token')
