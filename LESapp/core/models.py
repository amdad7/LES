
from django.db import models
from django.db.models.fields.json import JSONField
from accounts.models import Student
from django.utils import timezone

# Create your models here.
class Videos(models.Model):
    video_id=models.CharField(max_length=100,blank=False)
    title=models.CharField(max_length=500,blank=True)
    thumbnail=models.CharField(max_length=1000)
    average_viewtime=models.CharField(max_length=40,default=0)
    total_views=models.IntegerField(default=0)
    description=models.CharField(max_length=1000,blank=True)
    is_deleted=models.BooleanField(default=False)
    is_added=models.DateTimeField(default=timezone.now())
    
    
    def __str__(self):
        return self.title

    class Meta:
        ordering=['is_added']
           

class StudentVideoData(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    video=models.ForeignKey(Videos,on_delete=models.CASCADE)
    last_watched=models.DateTimeField(default=timezone.now())
    total_watched=models.IntegerField(default=0)
    timelist=models.TextField(max_length=500000,default='[]')

    def __str__(self):
        return self.video.title

    class Meta:
        unique_together=['student','video']

