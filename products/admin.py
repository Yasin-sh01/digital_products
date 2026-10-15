from django.contrib import admin

from products.models import Category, Product, File

class FileInline(admin.TabularInline):
    model = File

admin.site.register(Category)
admin.site.register(Product,  inlines = [FileInline])
admin.site.site_header = 'Digital Products Admin'