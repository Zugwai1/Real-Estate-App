from django.urls import path
from accommodation_support.views.property_view import PropertyView
from accommodation_support.views.property_detail_view import PropertyDetailView
from accommodation_support.views.property_search_view import PropertySearchView

urlpatterns = [
    path("", PropertyView.as_view()),
    path("<uuid:pk>", PropertyDetailView.as_view()),
    path("search/<str:filter>", PropertySearchView.as_view())
]
