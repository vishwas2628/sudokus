from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_to_sudoku_view, name='generate_image'),
]