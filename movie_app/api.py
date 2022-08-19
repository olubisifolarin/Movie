from urllib import response
from ninja import NinjaAPI, Form
from ninja.security import HttpBearer
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from ninja.errors import ValidationError
from django.http import HttpRequest
from .models import Movie,Login
from .schemas import MovieInSchema, MovieOutSchema, SignOutSchema, LoginSchema
from typing import List
from django.shortcuts import get_object_or_404


api = NinjaAPI()

class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":
            return token

@api.post("/signup", response=List[SignOutSchema])
def signup(request, username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    return {'username': username, 'email' :email, 'password': '*****'}

@api.post("/login", response=List[LoginSchema], auth=AuthBearer())
def login(request, username: str = Form(...), password: str = Form(...) ):
    try:
        user_model = get_user_model().objects.get(username=username)
    except get_user_model().DoesNotExist:
        raise ValidationError

    passwords_match = check_password(password, user_model.password)
    if not passwords_match:
        raise ValidationError
    return {"token": request.auth, 'username': username,'password': '*****'}
    

@api.get('/movie', response=List[MovieOutSchema])
def get_all_movie(request:HttpRequest):
    all_movie=Movie.objects.all()
    return all_movie

@api.post('/movie', auth=AuthBearer(), response={201:MovieOutSchema})
def create_a_movie(request:HttpRequest, payload:MovieInSchema):
    new_movie=Movie.objects.create(**payload.dict())
    return 201, new_movie

@api.get('/movie/{movie_id}', auth=AuthBearer(), response={200:MovieOutSchema})
def get_one_movie(request:HttpRequest, movie_id:int):
    movie = get_object_or_404(Movie, pk=movie_id)
    return 200, movie

@api.put('/movie/update/{movie_id}', auth=AuthBearer(), response={200:MovieOutSchema})
def update_movie(request:HttpRequest, movie_id:int, payload:MovieInSchema):
    post_to_update=get_object_or_404(Movie, pk=movie_id)
    post_to_update.title = payload.title
    post_to_update.description = payload.description
    post_to_update.save()
    return 200, post_to_update

@api.delete('/movie/delete/{movie_id}', auth=AuthBearer(), response={204:None})
def delete_movie(request:HttpRequest, movie_id:int):
    post_to_delete=get_object_or_404(Movie, pk=movie_id)
    post_to_delete.delete()
    return 204, None
