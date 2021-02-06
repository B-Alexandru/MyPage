
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('/abstract', views.abstarct, name="abstract"),
    
]
