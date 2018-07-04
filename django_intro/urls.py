"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from intro.views import get_todo_list, create_item, edit_item, toggle_status

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', get_todo_list),
    path(r'add', create_item),
    path(r'edit/<int:id>/', edit_item),
    path(r'toggle/<int:id>', toggle_status)
]
