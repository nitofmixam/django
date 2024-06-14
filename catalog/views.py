from django.shortcuts import render
from catalog.models import Product


# def home(request):
#     return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name)
        print(phone)
        print(message)
    return render(request, "contacts.html")


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "product_list.html", context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, "product_detail.html", context)
