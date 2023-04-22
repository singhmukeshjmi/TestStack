from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from teststack.serializers import *
from rest_framework import viewsets
from rest_framework.response import Response

class BugViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Bug.objects.all()
        serializer = BugSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Bug.objects.all()
        bug = get_object_or_404(queryset, pk=pk)
        serializer = BugSerializer(bug)
        return Response(serializer.data)