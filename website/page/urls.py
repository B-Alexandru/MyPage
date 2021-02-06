
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('abstract.html', views.abstract, name="abstract"),
    
]
