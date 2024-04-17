from django.contrib import admin

from ads.models import Ad, Comment

# TODO здесь можно подкючить ваши модели к стандартной джанго-админке
@admin.register(Ad)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'description', 'author', 'created_at')


@admin.register(Comment)
class UserAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'ad', 'created_at')
