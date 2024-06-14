from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import product_list, product_detail, contact


app_name = CatalogConfig.name

urlpatterns = [
    path("", product_list, name="index"),
    path("products/<int:pk>/", product_detail, name="product_detail"),
    path("contact/", contact, name="contact"),
]