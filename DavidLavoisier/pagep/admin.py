from django.contrib import admin
from .models import Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'image1')
    search_fields = ['nom']


admin.site.register(Article, ArticleAdmin)