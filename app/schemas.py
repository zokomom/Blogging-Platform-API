from pydantic import BaseModel

class PostIn(BaseModel):
    title:str
    content:str
    category:str
    tags:list[str]
    model_config={
        "from_attributes":True
    }

class PostUpdate(PostIn):
    pass

class PostOut(BaseModel):
    id:int=1
    title:str
    content:str
    category:str
    tags:list[str]
    created_at:str="Today"
    updated_at:str="Today"