from django.urls import path,include
from .views import *

app_name='teacher'

urlpatterns=[
    path('updatedb/',Update_video_db,name="updatedb"),
    path('adminclass/',adminclass,name="adminclass")
]