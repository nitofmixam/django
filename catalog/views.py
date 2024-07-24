from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, VersionFormSet, ProductModeratorForm
from catalog.models import Product, Contact, Version, Category
from catalog.services import get_categories_from_cache, get_products_from_cache


class ProductListView(ListView):
    """
    Контроллер, который отвечает за отображение списка продуктов
    """
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        list_product = Product.objects.all()

        for product in list_product:
            version = Version.objects.filter(product=product)
            activ_version = version.filter(is_active=True)
            if activ_version:
                product.active_version = activ_version.last().name
                product.number_version = activ_version.last().number
            else:
                product.active_version = 'Нет активной версии'

        context_data['object_list'] = list_product
        return context_data

    def get_queryset(self):
        return get_products_from_cache()


class ProductDetailView(DetailView):
    """
    Контроллер, который отвечает за отображение информации о конкретном продукте
    """
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    Контроллер, который отвечает за создание продукта
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """
    Контроллер, который отвечает за редактирование продукта
    """
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:products_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, formset=VersionFormSet, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if (user.has_perm('catalog.can_edit_description') and user.has_perm('catalog.can_edit_category')
                and user.has_perm('catalog.can_change_is_published')):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контроллер, который отвечает за удаление продукта
    """
    model = Product
    success_url = reverse_lazy('catalog:products_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or self.request.user.is_superuser:
            return self.object
        raise PermissionDenied


class CategoryListView(LoginRequiredMixin, ListView):
    """
    Контроллер, который отвечает за отображение списка категорий
    """
    model = Category

    def get_queryset(self):
        return get_categories_from_cache()


class ContactCreateView(CreateView):
    """
    Контроллер, который отвечает за отображение контактной информации
    """
    model = Contact
    fields = (
        "name",
        "phone",
        "message",
    )
    success_url = reverse_lazy("catalog:contacts")