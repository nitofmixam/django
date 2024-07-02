from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, ProductsListView, ProductsDetailView, ProductsCreateView, ProductsUpdateView, \
    ProductsDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', home),
    path('contacts/', contacts, name='contacts'),
    path('create/', ProductsCreateView.as_view(), name='create'),
    path('view/', ProductsListView.as_view(), name='list'),
    path('view/<int:pk>', ProductsDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ProductsUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductsDeleteView.as_view(), name='delete')
]