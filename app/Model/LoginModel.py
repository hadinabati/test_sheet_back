from app.Database import DATAbase
import datetime
from persiantools.jdatetime import JalaliDate

collection = DATAbase.userCollection
today_date = JalaliDate(JalaliDate.today()).strftime("%Y_%m_%d")
hour = datetime.datetime.now().hour
miniute = datetime.datetime.now().minute
times = '{}:{}'.format(hour, miniute)





def insert_user(data: dict):
    try:
        collection.insert_one(data)
        return True
    except:
        return False





