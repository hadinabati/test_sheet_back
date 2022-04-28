from fastapi import APIRouter, Request
from app.schema import StudentSchema as models
from app.Database import DATAbase
from app.Error import error_list
from pydantic import BaseModel, BaseConfig
from persiantools.jdatetime import JalaliDate, JalaliDateTime
from fastapi.templating import Jinja2Templates
import secrets
import datetime
import pytz
from typing import Optional

collection = DATAbase.student_database

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




@router.post('/insert_student', tags=['student'])
async def Insert(item: models.insert_student):
    try:
        data = {}
        data['name'] = item.name
        data['family'] = item.family
        data['token'] = secrets.token_hex(nbytes=8)
        data['age'] = item.age
        data['discription'] = item.description
        data['manager_code'] = item.manager_code
        data['school_code'] = item.school_code
        data['Gender'] = item.Gender
        data['class_token'] = item.paye_token
        data['class_name'] = item.paye_name

        res = await  collection.insert_one(data)
        if res:
            return {
                'OK': True
            }
        else:
            return {
                'OK': False
            }
    except:
        return {
            'OK': False
        }


@router.post('/student_list', tags=['student'])
async def student_list(item: models.get_list_student):
    try:
        query = {'$match': {'manager_code': item.manager_code, 'school_code': item.school_code}}
        result = await collection.aggregate([query]).to_list(None)
        data = []
        mydic = {}
        counter = 0
        for x in range(0, len(result)):
            mydic['name'] = result[x]['name']
            mydic['family'] = result[x]['family']
            mydic['token'] = result[x]['token']
            mydic['age'] = result[x]['age']
            mydic['Gender'] = result[x]['Gender']
            mydic['discription'] = result[x]['discription']
            mydic['class_token'] = result[x]['class_token']
            mydic['class_name'] = result[x]['class_name']
            counter = counter + 1
            data.append(mydic)
            mydic = {}

        return {
            'OK': True,
            'data': data,
            'counter': counter
        }
    except:
        return {
            'OK':False
        }


@router.delete('/delete_student', tags=['student'])
async def student_delete(item: models.delete_student):
    try:
        res = await collection.delete_many(
            {'token': item.student_token, 'manager_code': item.manager_code, 'school_code': item.school_code})
        if res:
            return {
                'OK': True
            }
        else:
            return {
                'OK': True,
                'res': False
            }
    except Exception as e:
        return {
            'error': e,
            'OK': False
        }


@router.put('/update_student', tags=['student'])
async def student_update(item: models.update_student):
    try:
        query = {'$set': {'name': item.name, 'family': item.family, 'age': item.age, 'discription': item.description,
                          'Gender': item.Gender}}
        res = await  collection.update_one({'token': item.student_token}, query)
        if res:
            return {
                'OK': True
            }
        else:
            return {
                'OK': True,
                'res': False
            }
    except Exception as e:
        return {
            'error': e,
            'OK': False
        }
