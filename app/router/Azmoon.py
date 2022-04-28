from fastapi import APIRouter
from app.schema import AzmoonSchema as models
from app.Database import DATAbase
from persiantools.jdatetime import JalaliDate, JalaliDateTime
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


@router.post('/create_azmoon', tags=['Azmmon'])
async def create_azmoon(item: models.create_azmoon):
    try:
        await  collection.update_one({'token': item.manager_code}, {
            '$push': {'Azmoon': {
                'name': item.name,
                'date': item.date,
                'student_list': item.student_list,
                'lesson_list': item.lesson_list,
                'is_correct': False,
                'keys': item.key,
                'token': secrets.token_hex(nbytes=8),
                'traz': item.traz,
                'has_negetive': item.negetive,
                'question_number': item.question_number

            }}
        })
        return {
            'OK': True
        }
    except:
        return {
            'OK': False
        }


@router.delete('/delete_azmoon', tags=['Azmmon'])
async def delete_azmoon(item: models.delete_azmoon):
    try:
        await collection.update_one({'token': item.manager_code}, {'$pull': {
            'Azmoon': {'token': item.token}}})
        return {
            'OK': True ,
            'OK2':'bale'
        }
    except:
        return {
            'OK': False
        }


@router.get('/all_azmoon', tags=['Azmmon'])
async def all_azmoon(token: Optional[str]):
    try:
        res = await  collection.find_one({'token': token})
        if res:
            Azmoon_detail = res['Azmoon']
            return {
                'OK': True,
                'result': True,
                'items': Azmoon_detail
            }
        else:
            return {
                'OK': True,
                'result': False
            }
    except:
        return {
            'OK': False,
        }


@router.put('/update_azmoon', tags=['Azmmon'])
async def update_azmoon(item:models.create_azmoon , item2:models.delete_azmoon):
    try:
        res= await collection.update_one({'token': item2.manager_code}, {'$pull': {
            'Azmoon': {'token': item2.token}}})
        if res:
            await  collection.update_one({'token': item.manager_code}, {
            '$push': {'Azmoon': {
                'name': item.name,
                'date': item.date,
                'student_list': item.student_list,
                'lesson_list': item.lesson_list,
                'is_correct': False,
                'keys': item.key,
                'token': secrets.token_hex(nbytes=8),
                'traz': item.traz,
                'has_negetive': item.negetive,
                'question_number': item.question_number

            }}
        })
            return {
                'OK': True
            }
        else:
            return {
                'OK':False,
                'deleted':True
            }
    except:
        return {
            'OK': False
        }
