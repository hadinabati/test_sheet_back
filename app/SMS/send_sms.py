import requests

sms_key = 'D44E5FB7-3EE2-46FD-9E68-8C175A3115A9'


def send_OTP(random_number: int, phone_number: str):
    text = f'کد اهراز هویت شما: ' \
           f'{random_number}'
    url = f'http://sms.parsgreen.ir/UrlService/sendSMS.ashx?from=10001398&to={phone_number}&&text={text}&&signature={sms_key}'
    res=requests.get(url=url)
    if res.status_code ==200 :
        return True
    else:
        return False


def Login(name:str ,  phone_number: str):
    text = f'کاربر گرامی : ' \
           f'{name}' \
           f'\n خوش آمدید '
    url = f'http://sms.parsgreen.ir/UrlService/sendSMS.ashx?from=10001398&to={phone_number}&&text={text}&&signature={sms_key}'
    res=requests.get(url=url)
    if res.status_code ==200 :
        return True
    else:
        return False


def send_password(new_pass: int, phone_number: str):
    text = f'رمز ورود شما : ' \
           f'{new_pass}' \
           f'\n' \
           f'لطفا بعد از ورود سریعا رمز خود را تغییر دهید '
    url = f'http://sms.parsgreen.ir/UrlService/sendSMS.ashx?from=10001398&to={phone_number}&&text={text}&&signature={sms_key}'
    res=requests.get(url=url)
    if res.status_code ==200 :
        return True
    else:
        return False
