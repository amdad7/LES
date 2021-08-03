from django.urls import path,include
from .views import *

app_name='core'

urlpatterns=[
    path('',Home),
    path('getvideos/',getvideos,name="getvideos"),
    path('getinfo/',getinfo,name="getinfo"),
    path('home/',Home,name="home"),
    path('gallery/<int:page>/',Gallery,name="gallery"),
    path('getfullvideostatus/',getfullvideostatus,name="getfullvideostatus"),
    path('video/<slug:slug>/',videoview,name="videoview"),
    path('postvdata/',postvdata,name="postvdata"),
    path('dashboard/',dashboard,name="dashboard"),
    path('noticeboard/',noticeboard,name="noticeboard")
]