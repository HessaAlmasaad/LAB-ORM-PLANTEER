from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from plants.models import Plant
# Bonus
from .models import Contact
# Create your views here.

def index_view(request):
    plants = Plant.objects.all()[0:3]
    print(plants.count())  
    return render(request, 'main/index.html', {'plants': plants}) 

def contact_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message
        )
        return redirect('main:contact_messages_view')  # Redirect after saving

    return render(request, 'main/contact.html')

def contact_messages_view(request):
    contacts = Contact.objects.all()
    return render(request, 'main/contact_messages.html', {'contacts': contacts})
