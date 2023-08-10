from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.todo,name='home'),
    path('update_task/<str:pk>/',views.update_task,name='update_task'),
    path('delete_task/<str:pk>/',views.delete_task,name='delete_task'),
    path('count',views.counts,name='counts')
]