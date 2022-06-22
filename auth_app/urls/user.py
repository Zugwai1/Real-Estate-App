from django.urls import path
from auth_app.views.user import UserView

urlpatterns = [
    path('register', UserView.as_view()),
    path('<uuid:pk>', UserView.as_view())
]
