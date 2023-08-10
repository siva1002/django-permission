from django import views
from django.urls import path
from . import views
urlpatterns=[
    path('',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('profile',views.create_profile,name='profile'),
    path('viewprofile',views.viewprofile,name='viewprofile'),
    path('signout',views.signout,name='signout'),
    path('update',views.update_profile,name='update'),
    path('home',views.home,name='home'),
    path('delete_user',views.delete_user,name='delete_user'),
    path("api",views.Adduser.as_view())
]