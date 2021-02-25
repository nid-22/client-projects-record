from django.shortcuts import render, redirect ,HttpResponse
from .forms import client_form, project_form, Login_form
from records_app.models import Client,UserInfo,Project,User
from django.contrib.auth import login as dj_login, logout as dj_logout ,authenticate

# Create your views here.
def home(request):    
    return render(request,'home_before_login.html')



def homepage(request):
    id=request.session.get('uid')
    u=User.objects.filter(user_id=id)
    return render(request,'home.html')

def client_register(request):
    if request.method == "POST":
        s = client_form(request.POST)
        s.save()
        return redirect('/')
    else:        
        return render(request,'form.html',{'form': client_form, 'name':'client register'})

def add_project(request):
    if request.method == "POST":
        s = project_form(request.POST)
        s.save()
        return redirect('/')
    else:        
        return render(request,'form.html',{'form': project_form, 'name':'project'})


def project_list(request):
    uid=request.session.get('uid')
    objects=Project.objects.filter(created_by=uid)
    return render(request, 'project_list.html', {'objects':objects})

def client_list(request):
    uid=request.session.get('uid')
    objects=Client.objects.filter(created_by=uid)
    return render(request, 'client_list.html', {'objects':objects})


def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            dj_login(request,user)
            request.session['uid']=user.id
            #id=request.session.get('uid')
            return render(request,'home.html',{'user':user})
            
            #return redirect('home')
        else:
            lmsg="invalid username and password"
            d = {'form':Login_form, 'lmsg':lmsg, "name":"login" }
            return render(request,'form.html',d)
    else: 
        return render(request,'form.html', {'form':Login_form , "name":"login"})

def logout(request):
    dj_logout(request)
    return redirect('/')

def delete_client(request,id):
    inc=Client.objects.get(id=id)
    inc.delete()
    return redirect('/')

def delete_project(request,id):
    exp=Project.objects.get(id=id)
    exp.delete()
    return redirect('/')

def update_client(request, id):
    inc = Client.objects.get(id=id)  
    if request.method=='POST':
        f=client_form(request.POST,instance=inc)
        f.save()
        return redirect('/client_list')
    else:
        f=client_form(instance=inc)
        return render(request,'form.html',{'form':f, "name":"Update"})

def update_project(request, id):
    inc = Project.objects.get(id=id)  
    if request.method=='POST':
        f=project_form(request.POST,instance=inc)
        f.save()
        return redirect('/project_list')
    else:
        f=project_form(instance=inc)
        return render(request,'form.html',{'form':f, "name":"Update"})


