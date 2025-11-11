from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
     path('',views.get_element,name='get_element'),
     path('get_users/<int:id>',views.get_users,name='get_users'),
     path('create_user',views.create_users,name='create_users'),
     path('update_users/<int:id>',views.update_users,name='update_users')
]
