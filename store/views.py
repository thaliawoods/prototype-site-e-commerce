from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse

from store.models import Products

# Create your views here.
def index(request):
    products = Products.objects.all()
    # return HttpResponse("Bonjour")
    return render(request, 'store/index.html', context={"products": products})

def product_detail(request, slug):
    # return HttpResponse(slug)
    product = get_object_or_404(Products, slug=slug)
    return render(request, 'store/detail.html', context={"product": product})