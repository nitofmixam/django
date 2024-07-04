from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsTemplateView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_catalog'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('blog/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('blog/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete')


]