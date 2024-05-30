from django.contrib import admin
from .models import Post, Comment


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']  # отображение полей в списке сущностей
    list_filter = ['status', 'created', 'publish', 'author']  # фильтрация по полям (в правой части экрана)
    search_fields = ['title', 'body']  # выбор полей для поиска
    prepopulated_fields = {'slug': ('title',)}  # автозаполнение поля
    raw_id_fields = ['author']  # создание поискового виджета
    date_hierarchy = 'publish'  # добавление иерархии по датам публикации (под строкой поиска)
    ordering = ['status', 'publish']  # автосортировка по полям


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
