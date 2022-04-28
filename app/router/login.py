from fastapi import APIRouter, Request
from app.schema import loginSchema as models
from app.Database import DATAbase
from app.Error import error_list
from app.SMS import send_sms
from app.Model import LoginModel as db
from app.Others import hashing
from persiantools.jdatetime import JalaliDate, JalaliDateTime
import random
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




@router.post('/send_SMS', tags=['login'])
async def Send_SMS(item: models.send_SMS):
    random_number = random.randint(a=10000, b=99999)
    result = send_sms.send_OTP(random_number=random_number, phone_number=item.phone)
    if result:
        return {
            'number': random_number
        }
    else:
        return {
            'error': error_list.errors.sms_not_send[0],
            'error_code': error_list.errors.sms_not_send[1]
        }


@router.post('/create', tags=['login'])
async def create_user(item: models.create_user):
    data = {}
    token = secrets.token_hex(nbytes=12)
    data['username'] = item.username
    data['name'] = item.name
    data['phone'] = item.phone
    data['email'] = item.email
    data['passwords'] = hashing.hash_password(item.passwords)
    data['token'] = token

    query = {'$match': {'username' : item.username}}
    result = await collection.aggregate([query]).to_list(None)

    if len(result) >0 :
        return {
            'OK': False,
            'error': 'خطا در ثبت کاربر'
        }
    else:
        result = db.insert_user(data=data)
        if result:
            try:
                send_sms.Login(name=item.name, phone_number=item.phone)
            except:
                pass

            return {
                'OK': True,
            }
        else:
            return {
                'OK': False,
            }


@router.post('/login', tags=['login'])
async def Login(item: models.input_login, req: Request):
    try:
        passwords = hashing.hash_password(item.passwords)
        query = {
            'username': item.username,
            'passwords': passwords
        }
        counter = await collection.count_documents(query)
        if counter > 0:
            finder = await collection.find_one(query)
            await collection.update_one({'token': finder['token']}, {'$set': {
                'time': times,
                'ip': req.client[0],
                'date': today_date,
                'day': name_of_day
            }})
            return {
                'OK': True,
                'result': 1,
                'username':item.username,
                'name': finder['name'],
                'emails': finder['email'],
                'token': finder['token'],
                'phone': finder['phone']

            }
        else:
            return {
                'OK': True,
                'result': 0,
            }
    except:
        return {
            'OK': False,
            'error': error_list.errors.loggin_server_error[0],
            'error_code': error_list.errors.loggin_server_error[1]
        }


@router.post('/forget', tags=['login'])
async def forget(item: models.token):
    try:
        randX = random.randint(a=10000, b=99999)
        print(randX)
        ress = send_sms.send_password(new_pass=randX , phone_number=item.phone)
        if ress:
            passwords = hashing.hash_password(str(randX))
            await collection.update_one({'phone': item.phone},
                                        {'$set': {'passwords': passwords,
                                                  'change_passwords': True,
                                                  'date_change_password': today_date,
                                                  'time_change_password': times}})
            return {
                'OK': True,
                'result': 1
            }
        else:
            return {
                'OK': True,
                'result': 0,
                'error': 'خطا در ارسال رمز جدید به مخاطب'
            }
    except Exception as e:
        print(e)
        return {
            'OK': False,
            'error': error_list.errors.forget_server_error[0],
            'error_code': error_list.errors.forget_server_error[1]
        }
