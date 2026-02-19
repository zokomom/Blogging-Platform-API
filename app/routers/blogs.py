from fastapi import APIRouter,status,Response,Depends
from sqlalchemy.orm import Session
from .. import schemas,models
from ..database import get_db
from typing import Optional,List


router=APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.PostOut)
def create_blog(blog:schemas.PostIn,db:Session=Depends(get_db)):
    created_blog=models.Post(**blog.model_dump())
    db.add(created_blog)
    db.commit()
    db.refresh(created_blog)
    return created_blog

@router.put("/{id}",status_code=status.HTTP_200_OK,response_model=schemas.PostOut)
def update_blog(id:int,blog:schemas.PostIn):
    return blog

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int):
    pass

@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=schemas.PostOut)
def get_post_by_id(id:int,db:Session=Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id==id).first()
    return post

@router.get("/",status_code=status.HTTP_200_OK,response_model=List[schemas.PostOut])
def get_all_posts(db:Session=Depends(get_db),term:Optional[str]=""):
    # get_all_posts_query=db.query(models.Post).filter(models.Post.title.contains(term)).all()
    posts=db.query(models.Post).all()
    return posts