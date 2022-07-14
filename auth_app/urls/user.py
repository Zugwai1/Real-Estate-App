from django.urls import path
from auth_app.views.user.user_view import UserView
from auth_app.views.user.user_details_view import UserDetailsView

urlpatterns = [
    path("", UserView.as_view()),
    path("<uuid:pk>", UserDetailsView.as_view())
]
