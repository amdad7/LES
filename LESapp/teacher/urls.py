from django.urls import path,include
from .views import *

app_name='teacher'

urlpatterns=[
    path('updatedb/',Update_video_db,name="updatedb"),
    path('adminclass/',adminclass,name="adminclass"),
    path('adminvideo/<slug:slug>/',adminvideo,name="adminvideo"),
    path('admingallery/<int:page>/',admingallery,name="admingallery"),
    path('adminstudentlist/',adminstudentlist,name="adminstudentlist"),
]