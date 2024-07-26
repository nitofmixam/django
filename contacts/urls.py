from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from contacts.views import ContactView
from contacts.apps import ContactsConfig

app_name = ContactsConfig.name

urlpatterns = [
    path("", ContactView.as_view(), name="contacts"),
]
