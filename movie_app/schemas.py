from dataclasses import dataclass
from datetime import datetime
from unicodedata import category
from ninja import Schema
from datetime import datetime

class SignOutSchema(Schema):
    username: str
    email: str
    password: str
    
class LoginSchema(Schema):
    username: str
    password: str
   

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
    
    