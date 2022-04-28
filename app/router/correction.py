from fastapi import APIRouter, File, UploadFile
from app.schema import correctionSchema as models
from app.Database import DATAbase
from persiantools.jdatetime import JalaliDate, JalaliDateTime
import secrets
import datetime
import pytz
from typing import Optional
import aiofiles
from starlette.responses import FileResponse
import os
from zipfile import ZipFile

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


@router.post("/uploadfile/", tags=['uploads'])
async def post_endpoint(in_file: UploadFile = File(...)):
    name = 'hadi'
    async with aiofiles.open(f'app//Files//uploaded//{name}.png', 'wb') as out_file:
        content = await in_file.read()
        await out_file.write(content)

    return {"Result": "OK"}


@router.post("/download/", tags=['uploads'])
async def download():
    file_path = os.getcwd() + "/" + "app" + "/" + "Files" + "/" + "uploaded" + "/" + "hadi.png"
    file_path2 = os.getcwd() + "/" + "app" + "/" + "Files" + "/" + "Zip" + "/" + "ziped.zip"
    zipObj = ZipFile(file_path2, 'w')
    zipObj.write(file_path)
    zipObj.close()

    return FileResponse(path=file_path2, filename='total.zip')
