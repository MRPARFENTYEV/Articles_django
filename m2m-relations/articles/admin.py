from django.contrib import admin

from .models import Article, Tag, Scope

# class OrderPositionInline(admin.TabularInline):
#     model =

# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ['id','title','text','published_at']
#     list_filter = ['id','title']

@admin.register(Tag)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','slug']


class RelationshipInline(admin.TabularInline):
    model = Scope
    extra = 5


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
    list_display = ['id','title','text','published_at']
    list_filter = ['id','title']