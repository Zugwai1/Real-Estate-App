from django.shortcuts import render


# Create your views here.

def signin(request):
    return render(request, 'auth/signin.html', context={})


def signup(request):
    return render(request, 'auth/signup.html', context={})
