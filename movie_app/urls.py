from django.urls import path
from movie_app import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.signin, name='login'),
]