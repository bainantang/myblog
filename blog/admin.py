from django.contrib import admin

from blog.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'put_time')
    list_filter = ('put_time',)


admin.site.register(Article, ArticleAdmin)

# Register your models here.
