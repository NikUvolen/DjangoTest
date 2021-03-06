from django.contrib import admin

from .models import Sells


class SellsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


admin.site.register(Sells, SellsAdmin)
