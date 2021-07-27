from django.db.models import fields
from .models import *
from rest_framework import serializers
from .models import *

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model =Videos
        fields=['video_id','title','thumbnail','description']

class StudentVideoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentVideoData
        fields=['last_watched','total_watched']