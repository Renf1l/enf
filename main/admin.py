from django.contrib import admin
from .models import Category, Product, ProductImage, ProductStock



class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductStockInline(admin.StackedInline):
    model = ProductStock
    can_delete = False
    verbose_name_plural = 'Stock'


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'manufacturer', 'stock', 'category', 'price']
    list_filter = ['category', 'manufacturer']
    search_fields = ['name', 'manufacturer', 'description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, ProductStockInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
