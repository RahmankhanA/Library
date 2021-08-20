from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, generics
from .Serializers import AddVideoSerializer
from  .models import AddVideo
# Create your views here.

class UploadVideo(generics.CreateAPIView):
    queryset= AddVideo.objects.all()
    serializer_class=AddVideoSerializer


class WatchVideo(generics.ListAPIView):
    queryset= AddVideo.objects.all()
    serializer_class=AddVideoSerializer

