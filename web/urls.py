from django.urls import path
from web.views.general_views import index
from web.views.auth_view import signin, signup

urlpatterns = [
    path("", index, name="index"),
    path("signin", signin, name="signin"),
    path("signup", signup, name="signup")
]
