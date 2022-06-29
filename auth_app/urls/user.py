from django.urls import path
from auth_app.views.user.user_view import UserView
from auth_app.views.user.user_details_view import UserDetailsView

urlpatterns = [
    path('list', UserView.as_view()),
    path('create', UserView.as_view()),
    path('get/<uuid:pk>', UserDetailsView.as_view()),
    path('edit/<uuid:pk>', UserDetailsView.as_view()),
    path('remove/<uuid:pk>', UserDetailsView.as_view())
]
