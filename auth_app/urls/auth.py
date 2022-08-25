from django.urls import path

from auth_app.views.auth.activation_view import activate
from auth_app.views.auth.auth_view import AuthView

urlpatterns = [
    path('token', AuthView.as_view()),
    path('activate/<str:uid>/<str:token>', activate)
]
