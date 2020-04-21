from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# /product --> index
def Index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})

def New(request):
    return HttpResponse("new product")