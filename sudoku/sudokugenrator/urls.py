from django.urls import path
from . import views

urlpatterns = [
    path("",views.sudoku_view,name="genrate")
]