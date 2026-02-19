from fastapi import FastAPI
from .routers import blogs
app=FastAPI()

app.include_router(blogs.router)

@app.get("/")
def root():
    return {"message":"Welcome to my blogging platform API!"}