from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Plant
# Bonus
from django.shortcuts import render, get_object_or_404
from django.http import Http404
import logging
from django.core.paginator import Paginator

logger = logging.getLogger(__name__)

# Create your views here.

def all_plants_view(request:HttpRequest):
    
    plant_list = Plant.objects.all()
    paginator = Paginator(plant_list, 10)  # Show 10 plants per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "plants/all_plants.html", {'page_obj': page_obj})


def plant_detail_view(request, plant_id):
    try:
        plant = get_object_or_404(Plant, id=plant_id)
    except Http404:
        return render(request, 'plants/404.html', status=404)
    return render(request, 'plants/plant_detail.html', {"plant": plant})


def create_plant_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        new_plant = Plant(
            name=request.POST.get("name"),
            about=request.POST.get("about"),
            used_for=request.POST.get("used_for"),
            image=request.FILES["image"], 
            category=request.POST.get("category"),
            is_edible=True if request.POST.get("is_edible") == "on" else False,
        ) 
        new_plant.save()

        return redirect("main:index_view")  

    return render(request, "plants/create.html")


def plant_update_view(request:HttpRequest, plant_id:int):

    plant = Plant.objects.get(pk=plant_id)

    if request.method == "POST":
        plant.name = request.POST["name"]
        plant.about = request.POST["about"]
        plant.used_for = request.POST["used_for"]
        if "plant" in request.FILES: plant.image = request.FILES["image"]
        plant.category=request.POST["category"]
        plant.is_edible = request.POST.get('is_edible', 'off') == 'on'
        plant.save()
        
        return redirect("plants:plant_detail_view", plant_id=plant_id)
    return render(request, "plants/plant_update.html", {"plant":plant})


def plant_delete_view(request:HttpRequest, plant_id:int):

    plant = Plant.objects.get(pk=plant_id)
    plant.delete()

    return redirect("main:index_view")


# plant_search_view



def custom_404_view(request, exception):
    return render(request, "posts/404.html", status=404)










