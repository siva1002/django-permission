
from django.shortcuts import redirect, render
from.form import *
from.models import *
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.

from rest_framework import permissions
from rest_framework import exceptions

@login_required
@permission_required("Todo_app.add_todo",raise_exception=True) 
def todo(request):
    task=Todo.objects.filter(user=request.user)
    form=do_form
    count=task.only('title').count()
    completed=task.filter(completed=1).count()
    processing=task.filter(completed=0).count()
    if request.method=='POST':
        form=do_form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user=request.user
            obj.remaining_time=obj.duetime
            obj=form.save()
            return redirect('/todo')
    context={'form':form,'task':task,'count':count,'completed':completed,'processing':processing}
    return render(request,'home.html',context)

@login_required(login_url='/signin')
def update_task(request,pk):
    task=Todo.objects.get(id=pk)
    form=do_form(instance=task)
    if request.method=='POST':
        form=do_form(request.POST,instance=task)
        if form.is_valid:
            obj = form.save(commit=False)
            obj.remaining_time=obj.duetime-obj.consumed_time
            form.save()
            return redirect('/todo')
    context={'form':form}
    return render(request,'update.html',context)

@login_required(login_url='/signin')
def delete_task(request,pk):
    item=Todo.objects.get(id=pk)
    item.delete()
    return redirect('/todo')

@login_required(login_url='/signin')
def counts(request):
      completed=Todo.objects.only('completed').count()
      context={'completed':completed}
      return render(request,'home.html',context)
