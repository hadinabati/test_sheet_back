from fastapi import APIRouter
from app.schema import payeSchema as models
from app.Database import DATAbase
from app.Error import error_list
from persiantools.jdatetime import JalaliDate, JalaliDateTime
import secrets
import datetime
import pytz

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


@router.post('/add_paye', tags=['paye'])
async def insert_paye(item: models.insert_paye):
    try:
        res = await  collection.update_one({'token': item.manager_code, 'Schools.token': item.school_code},
                                           {'$push': {
                                               'Schools.$.classes': {'name': item.name,
                                                                     'token': secrets.token_hex(nbytes=8)}}})
        if res:
            return {
                'OK': True,
                'result': True,
            }
        else:
            return {
                'OK': True,
                'result': False,
            }
    except:
        return {
            'OK': False,
            'error': error_list.errors.add_paye_school_error[0],
            'error_code': error_list.errors.add_paye_school_error[1]
        }


@router.post('/list_paye', tags=['paye'])
async def all_paye(item: models.paye_list):
    try:
        res = await collection.find_one({
            'token': item.manager_code
        })
        if res:
            clases_list = []
            for x in range(0, len(res['Schools'])):
                clases_list.append(res['Schools'][x]['classes'])
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
            'error': error_list.errors.add_paye_school_error[0],
            'error_code': error_list.errors.add_paye_school_error[1]
        }


@router.delete('/delete_paye', tags=['paye'])
async def insert_paye(item: models.delete_paye):
    try:

        doing = await collection.update_one({'token': item.manager_code, 'Schools.classes.token': item.paye_code},
                                            {'$pull': {'Schools.$.classes': {'token': item.paye_code}}})

        if doing:
            return {
                'OK': True,
                'result': True,
            }
        else:
            return {
                'OK': True,
                'result': False,
            }
    except Exception as e:
        return {
            'er': e,
            'OK': False,
            'error': error_list.errors.add_paye_school_error[0],
            'error_code': error_list.errors.add_paye_school_error[1]
        }
