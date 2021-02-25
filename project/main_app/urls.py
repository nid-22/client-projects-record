from django.contrib import admin
from django.urls import path, include
from . import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home),
    path('home/',v.home),
    path('home2/',v.homepage),
    path('userlogin/',v.login),
    path('logout/',v.logout),


    path('register/',v.client_register),
    path('addproject/',v.add_project),


    path('project_list/',v.project_list),
    path('client_list/',v.client_list),


    path('delete_client/<int:id>/',v.delete_client),
    path('delete_project/<int:id>/',v.delete_project),


    path('update_client/<int:id>/',v.update_client),
    path('update_project/<int:id>/',v.update_project),
]
