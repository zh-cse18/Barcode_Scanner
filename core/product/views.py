from django.shortcuts import render


# Create your views here.
from .models import Product
def index(request):
    context = {'products': Product.objects.all()}
    if request.method == 'POST':
        barcode_num = request.POST.get('barcode')
        length = len(barcode_num)
        print(length)
        if length==15:
            print(barcode_num)
            country = barcode_num[:2]
            manufacture = barcode_num[2:8]
            number = barcode_num[8:12]
            product = Product.objects.filter(number_id=number).filter(manufacture_id=manufacture).filter(country_id=country)

            print(country)
            print(manufacture)
            print(number)
            context = {
                'products': product
            }
            return render(request, 'index.html', context)
        else:
            name = barcode_num[:-2]
            print(name)
            product = Product.objects.filter(name=name)

            # print(country)
            # print(manufacture)
            # print(number)
            context = {
                'products': product
            }
            return render(request, 'index.html', context)

    return render(request, 'index.html', context)


# def index(request):
#     context = {'products': Product.objects.all()}
#     if request.method == 'POST':
#         barcode_num = request.POST.get('barcode')
#         length =len(barcode_num)
#         print(length)
#         # country = barcode_num[:2]
#         # manufacture = barcode_num[2:8]
#         # number = barcode_num[8:12]
#
#         #product = Product.objects.filter(number_id=number).filter(manufacture_id=manufacture).filter(country_id=country)
#         name = barcode_num[:-2]
#         print(name)
#         product = Product.objects.filter(name=name)
#
#
#         # print(country)
#         # print(manufacture)
#         # print(number)
#         context = {
#             'products': product
#         }
#         return render(request, 'index.html', context)
#
#     return render(request, 'index.html', context)
#
# def index(request):
#     context = {'products': Product.objects.all()}
#     if request.method == 'POST':
#         barcode_num = request.POST.get('barcode')
#         length = len(barcode_num)
#         print(length)
#         print(barcode_num)
#         country = barcode_num[:2]
#         manufacture = barcode_num[2:8]
#         number = barcode_num[8:12]
#         product = Product.objects.filter(number_id=number).filter(manufacture_id=manufacture).filter(country_id=country)
#
#         print(country)
#         print(manufacture)
#         print(number)
#         context = {
#             'products': product
#         }
#         return render(request, 'index.html', context)
#
#     return render(request, 'index.html', context)

