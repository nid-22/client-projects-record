from django.shortcuts import render,redirect

from .models import Client,UserInfo,Project,User
from .serializers import client_serializer, project_serializer, user_serializer




from rest_framework import generics, viewsets, permissions

def api(request):
    return render(request,'api.html')

class Create_client(generics.CreateAPIView):
    queryset=Client.objects.all()
    serializer_class=client_serializer

class Client_list(generics.ListAPIView):
    queryset=Client.objects.all()
    serializer_class=client_serializer

class Client_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = client_serializer

class Project_list(generics.ListAPIView):
    queryset=Project.objects.all()
    serializer_class= project_serializer

class Project_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class =project_serializer

class create_project(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class =project_serializer

from rest_framework.permissions import AllowAny
from rest_framework.decorators import  permission_classes

class create_user(generics.ListCreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = user_serializer
    permission_classes = (AllowAny,)

class user_list(generics.ListAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = user_serializer
    permission_classes = (AllowAny,)





