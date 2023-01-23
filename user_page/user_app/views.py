from django.shortcuts import render
from user_app.models import User
import os

# Create your views here.
def index(request):
    return render(request, os.path.join('user_app', 'index.html'))

def users(request):
    
    user_list = User.objects.order_by('first_name')
    user_dict = {"user":user_list}
    
    return render(request, os.path.join('user_app', 'users_page.html'), context=user_dict)