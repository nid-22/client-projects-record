from django.urls import path
from . import views as v

urlpatterns = [
    path('api',v.api),
    path('clientlist/',v.Client_list.as_view()),
    path('createuser/',v.create_user.as_view()),
    path('createclient/',v.Create_client.as_view()),
    path('createproject/',v.create_project.as_view()),
    path('client/<int:pk>/', v.Client_detail.as_view()),
    path('project/',v.Project_list.as_view()),
    path('project/<int:pk>/', v.Project_detail.as_view()),
    path('userlist/',v.user_list.as_view()),
    
]


