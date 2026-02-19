from pydantic import BaseModel
from datetime import datetime
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
    id:int
    title:str
    content:str
    category:str
    tags:list[str]
    createdAt:datetime
    updatedAt:datetime
    model_config={
        "from_attributes":True
    }