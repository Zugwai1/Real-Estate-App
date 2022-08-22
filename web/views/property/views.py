import uuid

from django.shortcuts import render


# Create your views here.

def list(request):
    return render(request, 'property/list.html', context={})


def single(request, id: uuid):
    return render(request, 'property/single.html', context={"property_id": id})


def create(request):
    return render(request, 'property/create.html', context={})


def contact(request, id: uuid):
    return render(request, 'property/contact.html', {"property_id": id})


def edit(request, id: uuid):
    return render(request, 'property/edit.html', {"property_id": id})
