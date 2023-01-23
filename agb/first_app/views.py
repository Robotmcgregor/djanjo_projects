from django.shortcuts import render
from django.http import HttpResponse
import os
from first_app.models import Topic, Webpage, AccessRecord


# Create your views here.

# def index(request):
#     return HttpResponse("Hello world")

# def index(request):
#     return HttpResponse('<H1>Biomass model</H1>')

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    # link to template tag in templates
    my_dict = {"insert_me" : "Now I am changed - Hello I am from views.py"}
    
    #return render(request, os.path.join("first_app", "index.html"), context=my_dict)
    return render(request, os.path.join("first_app", "index.html"), context=date_dict)

