from django.contrib import admin
from .models import Product, Seller, Company


class CompanyAdmin(admin.ModelAdmin):
    list_display  = ['name', 'address', 'email']


admin.site.register(Product)
admin.site.register(Seller)
admin.site.register(Company, CompanyAdmin)
