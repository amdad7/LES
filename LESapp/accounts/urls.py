from django.urls import path,include
from .views import *

app_name='accounts'

urlpatterns=[
    path('login/',login_user,name="login"),
    path('isloggedin/',is_loggedin,name="isloggedin"),
    path('logout/',logout_,name="logout"),
    path('changepass/',changepass,name="changepass")
]