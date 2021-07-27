from django.shortcuts import render
from rest_framework.serializers import Serializer
from .serializers import *
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from accounts.models import Student
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

def Home(request):
    return render(request,'core/home.html')
def getvideos(request):
    #print(request.GET.get('pgno'))
    pgno=int(request.GET.get('pgno'))
    nos=int(request.GET.get('nos'))
    print(pgno,nos)
    videos=Videos.objects.all()[(pgno-1)*nos:pgno*nos]
 
    serializer=VideosSerializer(videos,many=True)
    return JsonResponse(serializer.data,safe=False)

def getinfo(request):

    student_id=request.GET.get('user')
    video_id=request.GET.get('video')
    
    if student_id==None or video_id==None:
        return JsonResponse({'status':0,'messege':'failed'})
    try:
        video=Videos.objects.get(id=video_id)
        student=Student.objects.get(id=student_id)
        data=StudentVideoData.objects.all().get(student=student,video=video)
    except:
        return JsonResponse({'status':0,'messege':'failed'})  

    serializer=StudentVideoDataSerializer(data)
    return JsonResponse(serializer.data)    

def Gallery(request,page):
    
    return render(request,'core/gallery.html') 
    
    
