from django.urls import path
from . import views

app_name = 'file_upload'

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('success/', views.upload_success, name='upload_success'),
]
