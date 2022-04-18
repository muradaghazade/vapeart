from django.contrib import admin
from .models import *


admin.site.register([Filter, Image, Slider, Category, Brand, AboutUS, Shipping, FAQ, Order])


class ProductImageInline(admin.TabularInline):
    model = Image


class ProductFilterInline(admin.TabularInline):
    model = Filter


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductFilterInline, ProductImageInline]
    # raw_id_fields = ['brand']
    search_fields = ['title']

admin.site.register(Product, ProductAdmin)