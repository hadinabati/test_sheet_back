from fastapi import FastAPI
from app.router import login,school,paye,Student , lables ,Azmoon ,Lesson ,correction,Home
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/app/static", StaticFiles(directory="app/static"), name="static")

app.include_router(login.router)
app.include_router(school.router)
app.include_router(paye.router)
app.include_router(Student.router)
app.include_router(lables.router)
app.include_router(Azmoon.router)
app.include_router(Lesson.router)
app.include_router(correction.router)
app.include_router(Home.router)