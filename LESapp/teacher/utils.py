from django.contrib.auth.models import User
import requests
import json
from accounts.models import Teacher
from django.http import HttpResponseForbidden

def update():
    url='https://www.googleapis.com/youtube/v3/search'
    Authtoken='AIzaSyDm2ORFM0fxJXkOgWXm0nHvtoJgU2iaWV4'

    params={
        'key':Authtoken,
        'part':'snippet,id',
        'channelId':'UCDynU_X2sHSIc1RzUAVqgng',
        'maxResults':20,
        'order':'date'        
    }
    pageToken='start'

    vlis=[]
    while True:
        if pageToken==None:
            break
        elif pageToken=='start':
            pass
        else:
            params['pageToken']=pageToken
        res=requests.get(url,params=params)
        res=res.json()
        #print(res)
        #break
        
        pageToken=res.get('nextPageToken')
        lis=res.get('items')
       
        if lis==None:
            break
        for vid in res.get('items'):
            id=vid.get('id').get('videoId')
            title=vid.get('snippet').get('title')
            description=vid.get('snippet').get('description')
            thumbnail=f"https://img.youtube.com/vi/{id}/0.jpg"

            vlis.append({'id':id,'title':title,'description':description,'thumbnail':thumbnail})

    return vlis    


def teacher_required(fun):
    def inner(request,*args, **kwargs):
        try:
            user=request.user
            #print(user)
            teacher=Teacher.objects.get(user=user)
            #print(teacher)
            if not teacher:
                return HttpResponseForbidden()
            return fun(request,*args, **kwargs)   
        except:
            #print('err')
            return HttpResponseForbidden()

    return inner        


