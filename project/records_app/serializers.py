from .models import Client,UserInfo,Project,User
from rest_framework import serializers

class client_serializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class project_serializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class user_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('username','first_name', 'last_name', 'email', 'contact', 'password')

