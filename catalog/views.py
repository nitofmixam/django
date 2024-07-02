from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Category, Product


class ProductsCreateView(CreateView):
    """
    класс контроллер приложения каталог
    шаблон форма добавить продукт
    """
    model = Product
    fields = ('product_name', 'product_description', 'product_image', 'product_category', 'product_price')
    success_url = reverse_lazy('catalog:list')


class ProductsListView(ListView):
    """
    Класс контроллер приложения каталог
    шаблон продукты
    """
    model = Product
    template_name = 'catalog/products_list.html'


class ProductsDetailView(DetailView):
    """
    Класс контроллер приложения каталог
    шаблон продукта
    """
    model = Product
    template_name = 'catalog/products_detail.html'


class ProductsUpdateView(UpdateView):
    """
    класс контроллер приложения каталог
    шаблон форма изменить продукт
    """
    model = Product
    fields = ('product_name', 'product_description', 'product_image', 'product_category', 'product_price')
    success_url = reverse_lazy('catalog:list')

    def get_success_url(self):
        return reverse('products:detail', args=[self.kwargs.get('pk')])


class ProductsDeleteView(DeleteView):
    """
    класс контроллер приложения каталог
    шаблон форма удалить продукт
    """
    model = Product
    success_url = reverse_lazy('catalog:list')


def home(request):
    """
    Функция контроллер шаблона
    домашней страницы приложения каталог
    :param request: data
    :return: dict
    """
    category = Category.objects.all()
    context = {
        'object_list': category,
        'title': 'Главная'
    }
    return render(request, 'catalog/base.html', context)


def contacts(request):
    """
    Функция контроллер шаблона
    страницы контакты приложения каталог
    :param request: data
    :return: dict
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')

    context = {
        'title': 'Обратная связь'
    }
    return render(request, 'catalog/contacts.html', context=context)
