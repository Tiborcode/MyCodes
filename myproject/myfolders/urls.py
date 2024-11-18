from django.urls import path
from . import views

app_name = 'myfolders'

urlpatterns = [
    path('', views.upload_file, name='upload'),
    path('delete/<str:filename>/', views.delete_file, name='delete_file'),
    path('list/', views.list_files, name='list_files'),

]
