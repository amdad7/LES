from re import I
from .models import *
from accounts.models import *


def parselist(student,video):
    try:
        data=StudentVideoData.objects.get(student=student,video=video).timelist
        data=data[1:len(data)-1]
        arr=[]
        for i in data.split(','):
            try:
                arr.append(i)
            except:
                pass
        return arr
    except:
        s=StudentVideoData.objects.create(
            student=student,
            video=video
        )        
        s.save()
        return []     
def listtostring(lis):
    pass