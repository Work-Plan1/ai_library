from django.contrib import admin
from .models import Category, Comment, Book, Social_links, About, Image, Team


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'category')
    list_display_links = ('id', 'name', 'author')
    search_fields = ('name', 'author')
    list_filter = ('category', 'author')


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    filter_horizontal = ('social_medias',)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'occupation')
    list_display_links = ('id', 'full_name', 'occupation')


admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Book, BookAdmin)
admin.site.register(Social_links)
admin.site.register(About, AboutAdmin)
admin.site.register(Image)
admin.site.register(Team, TeamAdmin)
