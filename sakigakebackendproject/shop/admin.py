from django.contrib import admin

from shop.models import Shop

# Register your models here.
class ShopAdmin(admin.ModelAdmin):
    list_display=('name','location','category')

admin.site.register(Shop,ShopAdmin)