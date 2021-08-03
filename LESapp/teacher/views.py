from django.shortcuts import render
from django.shortcuts import render
from rest_framework.serializers import Serializer
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from accounts.models import Student
from django.contrib.auth.decorators import login_required
from .utils import *
# Create your views here.
from core.models import Videos,StudentVideoData
from accounts.models import Student
import datetime

@teacher_required
@login_required
def Update_video_db(request):
    vlis=update()
    for i in vlis:
       # print(i)
        if i['id']:
            v=Videos.objects.filter(video_id=i['id'])
            if len(v)<1:
                print(v)
                video=Videos.objects.create(
                    video_id=i['id'],
                    title=i['title'],
                    thumbnail=i['thumbnail'],
                    description=i['description']
                )
                video.save()
    return JsonResponse({'status':1,'messege':'successfully updated database'})            

@teacher_required
@login_required
def adminclass(request):
    return render(request,'teacher/adminclass.html')

#@teacher_required
@login_required
def adminvideo(request,slug):
    cls=request.GET.get('cls')
    v=Videos.objects.get(video_id=slug)
    return render(request,'teacher/adminvideo.html',{'cls':cls,'video':v.title})    

@teacher_required
@login_required
def admingallery(request,page):
    #print(page)
    cls=request.GET.get('cls')
    #print(cls)
    return render(request,'teacher/admingallery.html',{'cls':cls})


def adminstudentlist(request):
    try:
        order=request.GET.get('order')
        video_id=request.GET.get('video_id')
        cls=request.GET.get('cls')
        
        video=Videos.objects.get(video_id=video_id)
        #print('reachedhere')
        students=Student.objects.all().filter(section=cls)
        #print(video,students)
        lis=[]
        for st in students:
            try:
                data=StudentVideoData.objects.get(student=st,video=video)
                date=data.last_watched.strftime('%d/%m/%Y')
                lis.append([st.rollno,st.name,data.total_watched,date])
            except:
                lis.append([st.rollno,st.name,0,'never watched'])

        if order=="rollno":
            lis=sorted(lis,key=lambda x:x[1])
        else:
            lis=sorted(lis,key=lambda x:x[2],reverse=True)
        return JsonResponse({'status':1,'datalist':lis})
    except:
        return JsonResponse({'status':0,'messege':'something went!  wrong invalid query'})