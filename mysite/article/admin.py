from django.contrib import admin

from .models import ArticleColumn


class ArticleColumnAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ('column', 'created', 'user')
        list_filter = ('column', )
admin.site.register(ArticleColumn, ArticleColumnAdmin)
