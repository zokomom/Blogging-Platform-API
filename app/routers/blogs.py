from fastapi import APIRouter,status,Response
from .. import schemas

router=APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post_out)
def post_blog(blog:schemas.Post_in):
    return blog

