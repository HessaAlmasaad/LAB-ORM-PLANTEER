from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from plants.models import Plant
# Create your views here.

def index_view(request):
    plants = Plant.objects.all()[0:3]
    print(plants.count())  
    return render(request, 'main/index.html', {'plants': plants}) 

def contact_view(request: HttpRequest):

    return render(request, 'main/contact.html') 

def contact_messages_view(request: HttpRequest):

    return render(request, 'main/contact_messages.html') 


