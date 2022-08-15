from urllib import response
from ninja import NinjaAPI
from django.http import HttpRequest
from .models import Movie
from .schemas import MovieInSchema, MovieOutSchema
from typing import List
from django.shortcuts import get_object_or_404

api = NinjaAPI()

@api.get('/movie', response=List[MovieOutSchema])
def get_all_movie(request:HttpRequest):
    all_movie=Movie.objects.all()
    return all_movie

@api.post('/movie', response={201:MovieOutSchema})
def create_a_movie(request:HttpRequest, payload:MovieInSchema):
    new_movie=Movie.objects.create(**payload.dict())
    return 201, new_movie

@api.get('/movie/{movie_id}', response={200:MovieOutSchema})
def get_one_movie(request:HttpRequest, movie_id:int):
    movie = get_object_or_404(Movie, pk=movie_id)
    return 200, movie

@api.put('/movie/update/{movie_id}', response={200:MovieOutSchema})
def update_movie(request:HttpRequest, movie_id:int, payload:MovieInSchema):
    post_to_update=get_object_or_404(Movie, pk=movie_id)
    post_to_update.title = payload.title
    post_to_update.description = payload.description
    post_to_update.save()
    return 200, post_to_update

@api.delete('/movie/delete/{movie_id}', response={204:None})
def delete_movie(request:HttpRequest, movie_id:int):
    post_to_delete=get_object_or_404(Movie, pk=movie_id)
    post_to_delete.delete()
    return 204, None
