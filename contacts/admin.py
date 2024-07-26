from django.contrib import admin
from contacts.models import Contact

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    list_filter = ('name',)
    search_fields = ('name', 'phone', 'message')