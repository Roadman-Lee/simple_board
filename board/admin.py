from django.contrib import admin

# Register your models here.
from board.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'board_id', 'title', 'article', 'password', 'nickname', 'is_deleted']
    list_display_links = ['pk', 'board_id', 'title', 'article', 'nickname']
    list_filter = ['board_id', 'nickname', 'is_deleted']
    search_fields =['board_id', 'title', 'article', 'nickname']


