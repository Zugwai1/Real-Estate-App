from django.shortcuts import render
from auth_app.views.auth.activation_view import activate


# Create your views here.

def signin(request):
    return render(request, 'auth/signin.html', context={})


def signup(request):
    return render(request, 'auth/signup.html', context={})


def activate_user(request, uid: str, token: str):
    response = activate(request, uid, token)
    data = response.data
    return render(request, "auth/signin.html", {'message': data.get("message", ""), 'passed': data.get("passed", ""), 'form_activation' : True})
