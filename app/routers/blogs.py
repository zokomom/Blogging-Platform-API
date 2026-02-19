from fastapi import APIRouter,status,Response,Depends
from sqlalchemy.orm import Session
from .. import schemas
from ..database import get_db
from typing import Optional


router=APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.PostOut)
def post_blog(blog:schemas.PostIn,db:Session=Depends(get_db)):
    return blog

@router.put("/{id}",status_code=status.HTTP_200_OK,response_model=schemas.PostOut)
def update_blog(id:int,blog:schemas.PostIn):
    return blog

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int):
    pass

@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=schemas.PostOut)
def get_post_by_id(id:int):
    pass

@router.get("/",status_code=status.HTTP_200_OK,response_model=list[schemas.PostOut])
def get_all_posts(term:str=Optional[str]):
    pass