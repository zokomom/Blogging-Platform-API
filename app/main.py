from fastapi import FastAPI
from .routers import blogs
from . import models
from .database import engine

app=FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(blogs.router)

@app.get("/")
def root():
    return {"message":"Welcome to my blogging platform API!"}