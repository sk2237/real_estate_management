from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="listings/listings"),
    path('<int:listing_id>', views.listing,name="listings/listing"),
    path('search/', views.search,name="listings/search"),
]
