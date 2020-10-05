from django.contrib import admin

# Register your models here.
from product.models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    list_filter = ['category']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)