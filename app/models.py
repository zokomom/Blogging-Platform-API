from .database import Base
from sqlalchemy import Column,Integer,String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.dialects.postgresql import ARRAY

class Post(Base):
    __tablename__="blogs"

    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    content=Column(String,nullable=False)
    category=Column(String,nullable=False)
    tags=Column(ARRAY(String))
    createdAt=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    updatedAt=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

