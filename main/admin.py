from django.contrib import admin
from .models import Category, Size, Product, ProductSize, ProductImage

class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductSizeInLine(admin.TabularInline):
    model = ProductSize
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'color', 'price']
    list_filter = ['category', 'color']
    search_fields = ['name', 'color', 'description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInLine, ProductSizeInLine]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Product, ProductAdmin)