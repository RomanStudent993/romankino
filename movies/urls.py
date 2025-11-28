from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.film_list, name='film_list'),
    path('film/<int:pk>/', views.film_detail, name='film_detail'),
]

