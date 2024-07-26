from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from pytils.translit import slugify

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', "text", "preview", "publication")
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)    # преобразование заголовка в slug
            new_blog.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        """
        Переопределяем метод, чтобы показывать только опубликованные блоги
        """
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication=True)
        return queryset


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', "slug", "text", "preview", "publication")
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        """
         Переопределяем метод, чтобы при успешном сохранении редиректить на страницу детального продукта
        """
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):     #счетчик просмоитров
        self.object = super().get_object(queryset)    # возвращает объект с перемеными
        self.object.views += 1    # увеличивает счетчик просмотров
        self.object.save()    # сохраняет изменения
        return self.object