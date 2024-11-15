from django.urls import path
from . import views

app_name = 'myfolders'

urlpatterns = [
    path('', views.myfolders, name='folders'),


]
