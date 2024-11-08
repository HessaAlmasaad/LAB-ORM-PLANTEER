from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index_view(request: HttpRequest):

    return render(request, 'main/index.html') 

def contact_view(request: HttpRequest):

    return render(request, 'main/contact.html') 

def contact_messages_view(request: HttpRequest):

    return render(request, 'main/contact_messages.html') 


