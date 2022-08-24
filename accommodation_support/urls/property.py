from django.urls import path
from accommodation_support.views.property_view import PropertyView
from accommodation_support.views.property_detail_view import PropertyDetailView
from accommodation_support.views.property_search_view import PropertySearchView
from accommodation_support.views.property_sms_view import PropertySMSView
from accommodation_support.views.property_mail_view import PropertyMailView
from accommodation_support.views.property_user_view import PropertyUserView

urlpatterns = [
    path("", PropertyView.as_view()),
    path("<uuid:pk>", PropertyDetailView.as_view()),
    path("search", PropertySearchView.as_view()),
    path("sms", PropertySMSView.as_view()),
    path("email", PropertyMailView.as_view()),
    path("user", PropertyUserView.as_view())
]
