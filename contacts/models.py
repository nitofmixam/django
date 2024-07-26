from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя', help_text='Введите имя')
    phone = models.CharField(max_length=10, verbose_name='Телефон', help_text='Введите телефон(не более 10 символов)')
    message = models.TextField()

    def __str__(self):
        return f"{self.name} {self.phone}"

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ("name",)