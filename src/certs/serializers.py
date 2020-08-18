import pytz

from datetime                   import datetime
from django.contrib.auth.models import User
from rest_framework             import serializers

from .models                    import Project


class BaseSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source = 'creator.username')
    
    class Meta:
        abstract = True

class ProjectSerializer(BaseSerializer):
    
    description = serializers.CharField(
        max_length = 2000, 
        allow_blank = True, 
        trim_whitespace = True,
    )
    
    class Meta:
        model  = Project 
        fields = ('id', 'name', 'description', 'creator',)
