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
from core.models import Videos



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

def adminclass(request):
    return render(request,'teacher/adminclass.html')