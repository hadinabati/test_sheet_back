from pydantic import Field, BaseModel


class create_azmoon(BaseModel):
    name: str = Field(default=None, description='the name of Azmoon')
    date: str = Field(default=None, description='the date of Azmoon')
    negetive: bool = Field(default=True, description='if it is True it means that we have negetive mark')
    traz: int = Field(default=3000, description='traz')
    student_list: list = Field(default=[{"token": '' , 'info':{'name':'' ,'fname':"" , 'paye':"" , 'image_path':''}}], description='the list of student')
    lesson_list: list = Field(default=[{"lesson_token": '', "number_start": 0, 'number_finish': 0}],
                              description='the list of lessons')
    key: list = Field(default=[{"lesson_token": '', "number_Question": 0, 'answer_question': 0}])
    question_number: int = Field(default=0, description='the number of question')
    manager_code: str = Field(default=None, description='the manager_code')
    result:list=Field(default=[{'student_token' :'', 'upload_path':'' , 'correct_path':"" ,'result':[{'question':''}]}])



class delete_azmoon(BaseModel):
    manager_code: str = Field(default=None, description='the manager_code')
    token: str = Field(default=None, description='the token of azmoon')