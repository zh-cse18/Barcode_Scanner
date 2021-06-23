from django.shortcuts import render


# Create your views here.
from .models import Product


def index(request):
    context = {'products': Product.objects.all()}
    if request.method == 'POST':
        barcode_num = request.POST.get('barcode')
        country = barcode_num[:2]
        manufacture = barcode_num[2:8]
        number = barcode_num[8:13]

        product = Product.objects.filter(number_id=number).filter(manufacture_id=manufacture).filter(country_id=country)
        print(barcode_num)
        print(country)
        print(manufacture)
        print(number)
        context = {
            'products': product
        }
        return render(request, 'index.html', context)

    return render(request, 'index.html', context)
