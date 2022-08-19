from django.contrib import admin
from .models import Category, Movie, Signup, Login

# Register your models here.
admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Signup)
admin.site.register(Login)

