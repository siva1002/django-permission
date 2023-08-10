from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from . import models
# Register your models here.
class PermissionCheck(admin.ModelAdmin):
    def has_permission(self,request):
        return True
    def has_add_permission(self,request):
        content=Permission.objects.get(codename='add_logentry')
        print(content.id,request.user.user_permissions)
        return True

admin.site.register(models.Todo,PermissionCheck)
