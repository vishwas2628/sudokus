from django.urls import path
from . import views

urlpatterns = [
    path('solver/', views.image_to_sudoku_view, name='generate_image'),
    path('', views.home_view, name='home'),
]