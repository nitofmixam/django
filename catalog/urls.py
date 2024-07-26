from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsView, ProductDetailView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name='product_list'),
    path("contacts/", ContactsView.as_view(), name='contacts'),
    path("product/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path("product/create/", ProductCreateView.as_view(), name='product_create'),
    path("product/update/<int:pk>/", ProductUpdateView.as_view(), name='product_update'),
]