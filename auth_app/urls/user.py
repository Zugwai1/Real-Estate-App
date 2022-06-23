from django.urls import path
from auth_app.views.user.UserView import UserView
from auth_app.views.user.UserDetailsView import UserDetailsView

urlpatterns = [
    path('', UserView.as_view()),
    path('register', UserView.as_view()),
    path('<uuid:pk>', UserDetailsView.as_view())
]
