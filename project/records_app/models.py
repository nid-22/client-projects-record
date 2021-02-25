from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Client(models.Model):
    client_name = models.CharField(max_length=50)
    businesss_address =  models.CharField(max_length=50,  default='work from home')
    email = models.CharField(max_length=75)
    project_type = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name

class UserInfo(User):
    contact = models.IntegerField()

class Project(models.Model):
    project_name=models.CharField(max_length=50)
    client_name=models.ForeignKey(Client,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name