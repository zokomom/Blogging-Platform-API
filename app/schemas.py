from pydantic import BaseModel

class Post_in(BaseModel):
    title:str
    content:str
    category:str
    tags:list[str]
    model_config={
        "from_attributes":True
    }

class Post_out(BaseModel):
    id:int=1
    title:str
    content:str
    category:str
    tags:list[str]
    created_at:str="Today"
    updated_at:str="Today"