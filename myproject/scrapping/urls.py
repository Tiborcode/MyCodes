from django.urls import path
from . import views


app_name = 'scrapping'

urlpatterns = [
    path('', views.scrapping, name='scrapping'),
    path('process/', views.process_text, name='process_text'),
    path('test/', views.test_function, name='test'),
]