from django.urls import path,include
from .views import *

app_name='core'

urlpatterns=[
    path('getvideos/',getvideos,name="getvideos"),
    path('getinfo/',getinfo,name="getinfo"),
    path('home/',Home,name="home"),
    path('gallery/<int:page>',Gallery,name="gallery")
]