from records_app.models import Client, Project
from django import forms
#from django.contrib.auth.forms import UserCreationForm

class client_form(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"

class project_form(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"

class Login_form(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(widget =forms.PasswordInput) 