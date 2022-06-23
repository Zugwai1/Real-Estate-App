from django.urls import path
from auth_app.views.auth.AuthView import AuthView

urlpatterns = [
    path('token', AuthView.as_view()),
]
