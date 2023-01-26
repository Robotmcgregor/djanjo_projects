from django.shortcuts import render
from appTwo.models import User
import os

# Create your views here.
def index(request):
    return render(request, os.path.join('appTwo', 'index.html'))

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {"users":user_list}
    
    return render(request, os.path.join('appTwo', 'users.html'), context=user_dict)
