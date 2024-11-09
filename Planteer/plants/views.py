from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Plant, Country
# Validation
from .forms import PlantForm
# Bonus
from django.shortcuts import render, get_object_or_404
from django.http import Http404
import logging
from django.core.paginator import Paginator

logger = logging.getLogger(__name__)

# Create your views here.
def create_plant_view(request):
    if request.method == "POST":
        plant_form = PlantForm(request.POST, request.FILES)
        if plant_form.is_valid():
            plant_form.save()
            return redirect('main:index_view')
    else:
        plant_form = PlantForm()

    countries = Country.objects.all()  
    return render(request, 'plants/create.html', {
        'plant_form': plant_form,
        'countries': countries
    })
    
def plant_detail_view(request, plant_id):
    try:
        plant = get_object_or_404(Plant, id=plant_id)
    except Http404:
        return render(request, 'plants/404.html', status=404)
    
    # Fetch related plants based on the same category, excluding the current plant
    related_plants = Plant.objects.filter(category=plant.category).exclude(id=plant.id)[:4]  
    
    print(related_plants)  # Debugging output to check the queryset
    
    return render(request, 'plants/plant_detail.html', {
        "plant": plant,
        "related_plants": related_plants
    })

    
def plant_update_view(request: HttpRequest, plant_id: int):
    plant = Plant.objects.get(pk=plant_id)

    if request.method == "POST":
        plant.name = request.POST["name"]
        plant.about = request.POST["about"]
        plant.used_for = request.POST["used_for"]
        if "image" in request.FILES:
            plant.image = request.FILES["image"]
        plant.category = request.POST["category"]
        plant.is_edible = request.POST.get('is_edible', 'off') == 'on'
        plant.save()

        # Update native_to field (assuming it's a many-to-many relationship)
        native_to_ids = request.POST.getlist("native_to")
        plant.native_to.set(native_to_ids)

        return redirect("plants:plant_detail_view", plant_id=plant_id)

    countries = Country.objects.all()  # Assuming you have a Country model to list all options
    return render(request, "plants/plant_update.html", {"plant": plant, "countries": countries})


def plant_delete_view(request:HttpRequest, plant_id:int):

    plant = Plant.objects.get(pk=plant_id)
    plant.delete()

    return redirect("main:index_view")

def custom_404_view(request, exception):
    return render(request, "posts/404.html", status=404)

def all_plants_view(request):
    category_filter = request.GET.get('category')
    is_edible_filter = request.GET.get('is_edible')

    plant_list = Plant.objects.all()

    if category_filter:
        plant_list = plant_list.filter(category=category_filter)
    if is_edible_filter:
        is_edible_bool = is_edible_filter.lower() == 'true'
        plant_list = plant_list.filter(is_edible=is_edible_bool)

    plant_list = plant_list.order_by('name')

    # Get unique categories for the dropdown
    categories = Plant.objects.values_list('category', flat=True).distinct()

    # Pagination
    paginator = Paginator(plant_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'plants/all_plants.html', {
        "page_obj": page_obj,
        "categories": categories,
    })


    return render(request, "plants/all_plants.html", {
        'page_obj': page_obj,
        'category_filter': category_filter,
        'is_edible_filter': is_edible_filter,
    })

# plant_search_view














