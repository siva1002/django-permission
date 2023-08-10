from django.shortcuts import render,redirect
from.models import Users,Profile
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from.form import profile_form
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView,
)
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework.status import (
    HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED, HTTP_206_PARTIAL_CONTENT,
    HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_203_NON_AUTHORITATIVE_INFORMATION, HTTP_206_PARTIAL_CONTENT,
    HTTP_403_FORBIDDEN
)
from rest_framework.response import Response
from .serializer import UserSerializer
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
def home(request):
    return render(request,'web.html')

def signup(request):
    password=request.POST.get('password')
    password2=request.POST.get('password2')
    if request.method=='POST' and password==password2:
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=Users.objects.create(email=email,password=password,username=username)
        user.save()
        return redirect('signin')
    return render(request,'index.html')

@api_view(http_method_names=['GET','POST'])
def signin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,username=email,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('/home')
    messages.error(request,'wrong credential')
    return render(request,'signin.html')

@login_required(login_url='/signin')
@permission_required('Todo_app.add_todo')
def create_profile(request):
    form = profile_form
    if request.method == 'POST':
        form = profile_form(request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user=request.user
            obj=form.save()
            return redirect('viewprofile')
        else:
            messages.error('some error accuired')
    context={'form':form}
    return render(request,'profile.html',context)

@login_required(login_url='/signin')
def update_profile(request):
    obj = Profile.objects.get(user = request.user)
    form = profile_form(instance=obj)
    if request.method == 'POST':
        form = profile_form(request.POST,instance=obj,files=request.FILES)
        if form.is_valid:
            form.save()
            return redirect('viewprofile')
    context ={'form':form}
    return render(request,'update.html',context)

@login_required(login_url='/signin')
def viewprofile(request):
    return render(request,'viewprofile.html')

def signout(request):
    logout(request)
    return redirect('signin')

@login_required(login_url='/signin')
def delete_user(request):
    profile=Users.objects.get(email=request.user)
    profile.delete()
    return redirect('signup')

class Adduser(ListAPIView,PermissionRequiredMixin):
    serializer_class=UserSerializer
    queryset=Users.objects.all()
    permission_required={
        'GET':"cliapp_viewuser",
        'POST':"cliapp_adduser",
    }
    def post(self, request, *args, **kwargs):
        if self.has_permission():
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "data": serializer.data}, status=HTTP_201_CREATED)
            return Response({"status": False, "data": serializer.errors}, status=HTTP_206_PARTIAL_CONTENT)
        return Response({"status": False, "data": "you dont have permision to add user"}, status=HTTP_403_FORBIDDEN)
        
    def get(self, request, *args, **kwargs):
        if self.has_permission():
            print(request.user.has_perm('cli_app.view_users'))
            querset=self.get_queryset()
            serializer=UserSerializer(querset,many=True)
            return Response({"status": True, "data": serializer.data}, status=HTTP_201_CREATED)
        return Response({"status": True, "data": []}, status=HTTP_201_CREATED)
        
        
