from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import BlogForm, NoneForm
from .models import Blog
from .apps import BlogConfig
from pytils.translit import slugify
from django.urls import reverse_lazy, reverse


# Create your views here.


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_view')
    extra_context = {
        'project_name': BlogConfig.name,
        'title': 'Создать блог'
    }
    login_url = "users:login"

    def form_valid(self, form):
        # получает на вход форму, изменяет в атрибуте slug, сохраняет в БД
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)  # запоминаем slug code
            owner = self.request.user  # запоминаем владельца
            new_blog.owner = owner
            new_blog.save()
        return super().form_valid(form)


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    extra_context = {
        'project_name': BlogConfig.name,
        'title': 'Список блогов',
    }


class BlogDetailView(DetailView):
    model = Blog
    extra_context = {
        'project_name': BlogConfig.name,
        'title': 'Детализация блога'
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_view += 1
        self.object.save()
        return self.object


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_view')
    extra_context = {
        'project_name': BlogConfig.name,
        'title': 'Обновление блога'
    }

    def get_form_class(self):
        try:
            self.request.user.groups.get(name='content_manager')
        except BaseException:
            return NoneForm
        else:
            return BlogForm

    def form_valid(self, form):
        # получает на вход форму, изменяет в атрибуте slug, сохраняет в БД
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(LoginRequiredMixin,  PermissionRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_view')

    def has_permission(self):
        return self.request.user.groups.filter(name='content_manager').exists()