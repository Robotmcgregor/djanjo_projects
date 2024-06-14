from django.urls import path
from appTwo import views

urlpatterns = [
    path(r'', views.users, name="users"),
]
