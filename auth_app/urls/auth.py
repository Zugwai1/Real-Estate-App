from django.urls import path
from auth_app.views.auth import AuthView

urlpatterns = [
    path('token', AuthView.as_view()),
]
