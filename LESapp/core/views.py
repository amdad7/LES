from django.shortcuts import render
from rest_framework.serializers import Serializer
from .serializers import *
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from accounts.models import Student
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.decorators.csrf import csrf_exempt
from .utils import parselist
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
    try:
        video_id=request.GET.get('video_id')
        user=request.user
        student=Student.objects.get(user=user)
        video=Videos.objects.get(video_id=video_id)
        vdata=StudentVideoData.objects.all().get(student=student,video=video)
        percentage=vdata.total_watched
        timelist=parselist(student,video)
        return JsonResponse({"status":1,'percentage':percentage,'timelist':timelist,'avpercentage':video.average_viewtime})
        
    except:
        try:
            video_id=request.GET.get('video_id')
            video=Videos.objects.get(video_id=video_id)
            #return JsonResponse({'status':0,'avpercentage':video.average_viewtime})
            return JsonResponse({'status':0,'percentage':0,'timelist':[],'avpercentage':video.average_viewtime})
        except:
            return JsonResponse({'status':0,'percentage':0,'timelist':[],'avpercentage':100})
    

     
   

@login_required
def getstatus(request):
    u=request.user
    v=Videos.objects.all()

def Gallery(request,page):
    return render(request,'core/gallery.html') 
    


def getfullvideostatus(request):   
    try:
        user=request.user
        s=Student.objects.get(user=user)
    except:
        data={}
        videos=Videos.objects.all()
        for v in videos:
            data[v.video_id]=v.average_viewtime
        return JsonResponse(({'status':0,"perc":data}))       
    videos=Videos.objects.all()
    data={}
    perc={}
    for v in videos:
        data[v.video_id]=parselist(s,v)
        d=StudentVideoData.objects.get(student=s,video=v)
        perc[v.video_id]=d.total_watched
    return JsonResponse({"status":1,"data":data,'perc':perc})

def videoview(request,slug):
    print(slug)
    return render(request,'core/video.html')

@login_required
@csrf_exempt
def postvdata(request):
    try:
        #print(request.POST)
        user=request.user
        s=Student.objects.get(user=user)
        video_id=request.POST.get('video_id')
        v=Videos.objects.get(video_id=video_id)
        data=StudentVideoData.objects.get(student=s,video=v)
        #print(s,v,data)
        st="["+request.POST.get('timelist')+"]"
        data.timelist=st
        #print(request.POST.get('percentage'))
        data.total_watched=int(request.POST.get('percentage'))
        #print(data.timelist)
        data.save()

        try:
            inipercentage=request.POST.get('inipercentage')
            tot=len(Student.objects.all())
            #v.average_viewtime=0
            v.average_viewtime= str(round(float(v.average_viewtime)+(float(data.total_watched)-float(inipercentage))/tot,2))
            v.save()
        except:
            print('something went wrong')

        return JsonResponse({'status':1})
    except:
        return JsonResponse({'status':0})