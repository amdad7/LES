from django.http.response import HttpResponseForbidden, JsonResponse
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
            try:
                u=Student.objects.get(user=user)
            except:
                u=Teacher.objects.get(user=user)
              
            login(request, user)    
            return JsonResponse({'status':1,'messege':'success','is_changed':u.is_changed})
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
        t=Teacher.objects.all().filter(user=request.user)
        data['teacher']=0
        if len(t)>0:
            data['teacher']=1
    return JsonResponse(data)    

@csrf_exempt
@login_required
def changepass(request):
    u=request.user
    username=u.username
    st=Student.objects.get(user=u)
    if request.method=="POST":
        username1=request.POST.get('username')
        password=request.POST.get('password')
        if username!=username1:
            return HttpResponseForbidden()
        else:
            u.set_password(password)
            u.save()
            st.is_changed=True
            st.save()
            return JsonResponse({'status':1})
            
    return render(request,'accounts/password.html',{'username':username})