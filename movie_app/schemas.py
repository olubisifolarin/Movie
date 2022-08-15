from dataclasses import dataclass
from datetime import datetime
from email.mime import image
from unicodedata import category
from ninja import Schema
from datetime import datetime

class MovieInSchema(Schema):
    title: str
    description: str
   
    
class MovieOutSchema(Schema):
    id: int
    title: str
    description: str
    created: datetime
    duration:int
    poster: str
    
    