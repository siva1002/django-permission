from django.db import models
from cli_app.models import Users

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=20)
    user = models.ForeignKey(Users,on_delete=models.SET_NULL,null=True)
    description=models.TextField(max_length=150,default='')
    created_date=models.DateField(auto_now_add=True)
    completed=models.BooleanField(default=False)
    duetime=models.IntegerField(default=0,blank=True)
    remaining_time=models.IntegerField(default=0,blank=True)
    consumed_time=models.IntegerField(default=0,blank=True)
    
    def __str__(self):
        return self.title