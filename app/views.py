from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from app.serliazers import *
from app.models import *

# Create your views here.
class HomeView(viewsets.ModelViewSet):
    serializer_class = EmailSerializer
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        return Email.objects.all()

    def list(self, request, *args, **kwargs):
        fake_list = [{"success":True,"message":"Api working fine!"}]
        #return JsonResponse(fake_list,status=200,safe=False)
        return super().list(request,*args,**kwargs)