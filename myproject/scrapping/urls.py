from django.urls import path
from . import views

app_name = 'scrapping'

urlpatterns = [
    path('', views.scrapping, name='scrapping'),


]