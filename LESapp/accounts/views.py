from django.http.response import JsonResponse
from django.shortcuts import render
from .models import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status':1,'messege':'success'})
        return JsonResponse({'status':0,'messege':'failed'})     
    else:
        return render(request,'accounts/login.html')


@login_required
def logout_(request):
    logout(request)
    return JsonResponse({'status':1,'messege':'succefully logged out'})


def is_loggedin(request):
    data={'status':False}
    if request.user.is_authenticated:
        data['status']=True
    return JsonResponse(data)    
