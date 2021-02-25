from django.contrib import admin


from .models   import Client,UserInfo,Project,User

class Client_admin(admin.ModelAdmin):
    list_display = ['client_name', 'businesss_address','email','project_type','created_at', 'created_by']
    list_filter = []

admin.site.register(Client,Client_admin)

class user_admin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','email', 'contact']
    list_filter = []

admin.site.register(UserInfo,user_admin)

class Project_admin(admin.ModelAdmin):
    list_display =['project_name','client_name','created_at','created_by' ,'updated_at']
    list_filter = []

admin.site.register(Project,Project_admin)

