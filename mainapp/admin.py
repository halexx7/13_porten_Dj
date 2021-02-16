from django.contrib import admin

from .models import Product, ProductCategory, Brands

admin.site.register(ProductCategory)
admin.site.register(Brands)
admin.site.register(Product)
