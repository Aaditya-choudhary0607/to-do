"""
URL configuration for todoapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# todoapp/urls.py
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add/', views.add_todo, name='add_todo'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
]
