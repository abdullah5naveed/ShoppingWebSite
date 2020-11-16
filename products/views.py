from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


#URL -> Uniform Resource Locator
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {"products":products})
    # return HttpResponse("Hello World...")


def new(request):
    return HttpResponse("New page of products...")
