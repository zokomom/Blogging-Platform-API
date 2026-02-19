from fastapi import APIRouter,status,Response,Depends,HTTPException
from sqlalchemy import or_
from sqlalchemy.orm import Session
from .. import schemas,models
from ..database import get_db
from typing import Optional,List
from datetime import datetime,timezone


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
def update_blog(id:int,blog:schemas.PostIn,db:Session=Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id==id)
    update_post=post.first()
    if update_post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The Blog with id: {id} does not exists")
    updated_post=blog.model_dump()
    updated_post["updatedAt"]=datetime.now(timezone.utc)
    post.update(updated_post)
    db.commit()
    return post.first()

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int,db:Session=Depends(get_db)):
    delete_post=db.query(models.Post).filter(models.Post.id==id).first()
    if delete_post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The Blog with id: {id} does not exists")
    db.delete(delete_post)
    db.commit()
    return {"message":"blog deleted successfully"}

@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=schemas.PostOut)
def get_post_by_id(id:int,db:Session=Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id==id).first()
    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The Blog with id: {id} does not exists")
    return post

@router.get("/",status_code=status.HTTP_200_OK,response_model=List[schemas.PostOut])
def get_all_posts(term: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(models.Post)
    if term:
        search = f"%{term}%"
        query = query.filter(
            or_(
                models.Post.title.ilike(search),
                models.Post.content.ilike(search),
                models.Post.category.ilike(search),
            )
        )
    return query.all()