from django.shortcuts import render
# from django.http import HttpResponse

from store.models import Products

# Create your views here.
def index(request):
    products = Products.objects.all()
    # return HttpResponse("Bonjour")
    return render(request, 'store/index.html', context={"products": products})

