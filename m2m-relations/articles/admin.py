from django.contrib import admin

from .models import Article, Tag, Scope

class Scopes(admin.TabularInline):
    model = Scope
    extra = 4

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [Scopes]

@admin.register(Tag)
class Tag(admin.ModelAdmin):
    list_display = ['id', 'name']





