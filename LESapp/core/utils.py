import requests
import requests
import json

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
            thumbnail=vid.get('snippet').get('thumbnails').get('default').get('url')

            link=f"https://www.youtube.com/watch?v={id}"

            vlis.append([link,title,description,thumbnail])
            
    return(vlis)    







