from django.contrib import admin
from .models import Story, Category


class StoriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'published', 'category']
    list_display_links = ['title', 'category']
    list_filter = ['title', 'published', 'category']
    search_fields = ['title', 'category']


admin.site.register(Story, StoriesAdmin)
admin.site.register(Category)
