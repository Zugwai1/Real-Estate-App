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


def search(request):
    return render(request, 'property/search.html', {
        'price': request.GET.get('price', 0),
        'location': request.GET.get('location', ""),
        'keyword': request.GET.get('keyword', 0),
        'number_of_bedrooms': request.GET.get('number_of_bedrooms', 0),
        'number_of_bathrooms': request.GET.get('number_of_bathrooms', 0),
    })
