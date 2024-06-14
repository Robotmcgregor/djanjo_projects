from django.shortcuts import render
from basicapp import forms

# Create your views here.
def index(requests):
    return render(requests, 'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()
    
    if request.POST:
        form = forms.FormName(request.POST) 
    
    # if request.method == "POST":
    #     form = forms.FormName(request.Post)
        
        if form.is_valid():
            # do something
            print("VALIDATION SUCESS")
            print("Name: " + form.cleaned_data['name'])
            print("email: " + form.cleaned_data['email'])
            print("Free text: " + form.cleaned_data['text'])
    
    
    return render(request, 'basicapp/form_page.html',{'form':form})