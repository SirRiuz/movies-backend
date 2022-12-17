

# Django
from django.contrib import admin


# Models
from .models import *


@admin.register(Movie)
class MoviesAdmin(admin.ModelAdmin):
    list_display = [ 'name','gender','views','score' ]


@admin.register(MovieView)
class MoviesAdmin(admin.ModelAdmin):
    list_display = [ 'user','movieItem' ]


@admin.register(MovieRating)
class MoviesAdmin(admin.ModelAdmin):
    list_display = [ 'user','movieItem','score' ]


