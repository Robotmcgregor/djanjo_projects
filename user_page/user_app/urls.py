
from django.urls import path
from user_app import views

urlpatterns = [
    path(r'', views.users_page, name="users"),
]
