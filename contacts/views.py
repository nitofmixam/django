from django.shortcuts import render
from django.views.generic import View
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
import os
from contacts.apps import ContactsConfig
from contacts.models import Contact


# Create your views here.


class ContactView(View):
    model = Contact
    content = {'project_name': ContactsConfig.name, 'title': 'Контакты'}
    extra_context = {}

    def get(self, request: WSGIRequest) -> HttpResponse:
        return render(request, os.path.join(ContactsConfig.name, "contact_form.html"), self.content)

    def post(self, request: WSGIRequest) -> HttpResponse:
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        contact = Contact()
        contact.name = name
        contact.phone = phone
        contact.message = message
        contact.save()  # сохраняет в БД
        resp = {'name': name, 'phone': phone, 'message': message, 'project_name': ContactsConfig.name}
        return render(request, os.path.join(ContactsConfig.name, "contact_form.html"), resp)
