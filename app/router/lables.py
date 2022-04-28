from fastapi import APIRouter, Request
from app.schema import lablesShema as models
from app.Database import DATAbase
from app.Error import error_list
from pydantic import BaseModel, BaseConfig
from persiantools.jdatetime import JalaliDate, JalaliDateTime
from fastapi.templating import Jinja2Templates
import secrets
import datetime
import pytz
from typing import Optional

collection = DATAbase.userCollection

templates = Jinja2Templates(directory=".\\app\\Reports")

today_date = JalaliDate(JalaliDate.today()).strftime("%Y_%m_%d")
date_spilted = today_date.split('_')
hour = datetime.datetime.now().hour
miniute = datetime.datetime.now().minute
times = '{}:{}'.format(hour, miniute)
prz = JalaliDateTime(int(date_spilted[0]), int(date_spilted[1]), int(date_spilted[2]), hour, miniute, 0, 0,
                     pytz.utc).strftime("%c")
name_of_day = prz.split(' ')[0]

router = APIRouter()


@router.post('/add_lable', tags=['lables'])
async def add_lable(item: models.insert_Lable):
    try:
        await  collection.update_one({'token': item.manager_code}, {'$push': {'lables': {'name': item.name,
                                                                                         'student_list': item.student_info,
                                                                                         'token': secrets.token_hex(
                                                                                             nbytes=8)}}})
        return {
            'OK': True
        }
    except:
        return {
            'OK': False
        }


@router.delete('/delete_lable', tags=['lables'])
async def delete_lable(item: models.delete_lable):
    try:
        await  collection.update_one({'token': item.manager_code}, {
            '$pull': {'lables': {'token': item.token}}
        })
        return {
            'OK': True
        }
    except:
        return {
            'OK': False
        }


@router.post('/get_lables' , tags=['lables'])
async def lables_list(item: models.lables_list):
    try:
        query = {'$match': {'manager_code': item.manager_code}}
        result = await collection.aggregate([query]).to_list(None)
        data = []
        mydic = {}
        counter = 0
        for x in range(0, len(result)):
            mydic['name'] = result[x]['lables']['name']
            mydic['student_list'] = result[x]["lables"]['student_list']
            mydic['token'] = result[x]["lables"]['token']
            counter = counter + 1
            data.append(mydic)
            mydic = {}

        return {
            'OK': True,
            'data': data,
            'counter': counter
        }
    except Exception as er :
        return {
            'OK':False,
            'er':er
        }


