#from django.core import serializers
from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = '__all__'