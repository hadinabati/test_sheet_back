from fastapi import APIRouter, Request
from app.schema import schoolschema as models
from app.Database import DATAbase
from app.Error import error_list
from persiantools.jdatetime import JalaliDate, JalaliDateTime
from fastapi.templating import Jinja2Templates
import secrets
import datetime
import pytz

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


@router.post('/add_school', tags=['school'])
async def Add_school(item: models.addSchool):
    try:

        token = secrets.token_hex(nbytes=8)
        data = {}
        data['name'] = item.name
        data['address'] = item.address
        data['kind'] = item.kind
        data['token'] = token
        data['paye'] = item.paye
        res = await collection.update_one({'token': item.manager_code}, {'$push': {'Schools': data}})
        if res:
            return {
                'OK': True,
                'result': True

            }
        else:
            return {
                'OK': True,
                'result': False,
            }
    except:
        return {
            'OK': False,
            'error': error_list.errors.add_school_server_error[0],
            'error_code': error_list.errors.add_school_server_error[1]
        }


@router.delete('/delete_school', tags=['school'])
async def delete_school(item: models.delete_school):
    try:
        res = await collection.update_one({'token': item.manager_code}, {
            '$pull': {'Schools': {'token': item.school_code}}
        })
        if res:
            return {
                'OK': True,
                'result': True

            }
        else:
            return {
                'OK': True,
                'result': False,
            }
    except:
        return {
            'OK': False,
            'error': error_list.errors.delete_school_server_error[0],
            'error_code': error_list.errors.delete_school_server_error[1]
        }


@router.post('/schoo_list', tags=['school'])
async def school_list(item: models.school_list):
    try:
        res = await  collection.find_one({'token': item.manager_code})
        if res:
            scholl_details = res['Schools']
            return {
                'OK': True,
                'result': True,
                'items': scholl_details
            }
        else:
            return {
                'OK': True,
                'result': False
            }
    except:
        return {
            'OK': False,
            'error': error_list.errors.get_school_server_error[0],
            'error_code': error_list.errors.get_school_server_error[1]
        }


@router.get('/schoo_list_report', tags=['school'])
async def school_list_report(request: Request):
    try:
        lists=[{'name':'دخترانه راه رشد' , 'paye':'دوره دوم' , 'sex':'دخترانه' , 'row':1},{'name':'پسرانه راه رشد' , 'paye':'دوره اول' , 'sex':'پسرانه' , 'row':2}]
        return templates.TemplateResponse("school_report.html",
                                          context={'request': request, 'name': 'hadi', 'data': lists})
    except Exception as e:
        return {
            'er': e
        }
