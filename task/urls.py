from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="list"),
    path('Update_Task/<str:pk>/',views.updateTask,name="Update_Task"),
    path('delete/<str:pk>/',views.deleteTask,name="delete")
]