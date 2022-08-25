from django.urls import path
from web.views.general_views import index, profile, workspace
from web.views.property.views import list, single, create, contact, edit, search
from web.views.auth_view import signin, signup, activate_user

urlpatterns = [
    path("", index, name="index"),
    path("property/create", create, name="create"),
    path("property/contact/<uuid:id>", contact, name="contact"),
    path("profile", profile, name="profile"),
    path("property/list", list, name="list"),
    path('property/single/<uuid:id>', single, name='single'),
    path("signin", signin, name="signin"),
    path("signup", signup, name="signup"),
    path("workspace", workspace, name="workspace"),
    path('property/edit/<uuid:id>', edit, name="edit"),
    path(r'^property/search/$', search, name="search"),
    path('activate/<str:uid>/<str:token>', activate_user, name="activate")
]
