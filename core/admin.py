from django.contrib import admin

from core.models import DictRefType, Bookmark, Collection


@admin.register(DictRefType)
class DictRefTypeAdmin(admin.ModelAdmin):
    search_fields = ['type']
    list_display = ['type']


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    search_fields = ['id', 'title']
    list_display = ['id', 'title']


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']
    list_display = ['id', 'name']

