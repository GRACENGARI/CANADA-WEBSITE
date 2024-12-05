from django.shortcuts import render
from .models import Contact

# Create your views here.
# def index(request):
#     products = Product.objects.all()
#     context = {
#         'products': products,

#     }
#     return render(request, 'index.html', context)
        
def index(request):
    return render(request, 'index.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def service(request):
    return render(request, 'service.html')

def starter(request):
    return render(request,'starter.html')



 
 
 