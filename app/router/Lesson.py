from fastapi import APIRouter, Request
from app.schema import LessonSchema as models
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

today_date = JalaliDate(JalaliDate.today()).strftime("%Y_%m_%d")
date_spilted = today_date.split('_')
hour = datetime.datetime.now().hour
miniute = datetime.datetime.now().minute
times = '{}:{}'.format(hour, miniute)
prz = JalaliDateTime(int(date_spilted[0]), int(date_spilted[1]), int(date_spilted[2]), hour, miniute, 0, 0,
                     pytz.utc).strftime("%c")
name_of_day = prz.split(' ')[0]

router = APIRouter()


@router.post('/create_lesson', tags=['lesson'])
async def create_lesson(item: models.lesson_create):
    try:
        await collection.update_one({'token': item.manager_token, 'Schools.token': item.school_token}, {
            '$push': {
                'Schools.$.lesson': {'name': item.name, 'token_lesson': secrets.token_hex(nbytes=4), 'kind': item.kind,
                                     'des': item.description}}
        })
        return {
            'OK': True
        }
    except:
        return {
            'OK': False
        }


@router.delete('/delete_lesson', tags=['lesson'])
async def delete_lesson(item: models.lesson_delete):
    try:
        await collection.update_one({'token': item.manager_token, 'Schools.lesson.token_lesson': item.token}, {
            '$pull': {
                'Schools.$.lesson': {'token_lesson': item.token}}
        })
        return {
            'OK': True
        }
    except:
        return {
            'OK': False
        }


@router.post('/all_lesson', tags=['lesson'])
async def all_lesson(item: models.all_lesson):
    try:
        res = await collection.find_one({
            'token': item.manager_token
        })
        if res:
            clases_list = []
            for x in range(0, len(res['Schools'])):
                clases_list.append(res['Schools'][x]['lesson'])
            return {
                'OK': True,
                'result': True,
                'data': clases_list
            }
        else:
            return {
                'OK': True,
                'result': False,
            }
    except:
        return {
            'OK': False,
            'error': error_list.errors.list_error_lesson_get[0],
            'error_code': error_list.errors.list_error_lesson_get[1]
        }


