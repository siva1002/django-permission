from django.contrib import admin
from .models import Users,Profile
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# Register your models here.
class PermissionCheck(admin.ModelAdmin):
    def has_permission(self,request):
        return True
    def has_add_permission(self,request):
        return True 
    # if content.id in request.user.user_permissions or request.user.is_superuser else False 

admin.site.register(Users,PermissionCheck)
admin.site.register(Profile)
admin.site.register(Permission)