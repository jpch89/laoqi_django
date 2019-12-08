from django.urls import path

from . import views

app_name = 'image'

urlpatterns = [
    path('list-images/', views.list_images, name='list_images'),
    path('upload-image/', views.upload_image, name='upload_image'),
]
