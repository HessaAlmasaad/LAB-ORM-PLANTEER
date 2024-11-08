from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name="plants"

urlpatterns = [
    
    path("plants/all/", views.all_plants_view, name="all_plants_view"),
    path("plants/<plant_id>/detail/", views.plant_detail_view, name="plant_detail_view"),
    path('plants/new/', views.create_plant_view, name='create_plant_view'),
    path("plants/<plant_id>/update/", views.plant_update_view, name="plant_update_view"),
    path("plants/<plant_id>/delete/", views.plant_delete_view, name="plant_delete_view"),
    #path("plants/search/", views.plant_search_view, name="plant_search_view"),
    
    
] 
if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    # Custom error handlers
handler404 = 'plants.views.custom_404_view'
