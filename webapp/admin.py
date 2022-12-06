from django.contrib import admin
from .models import Products

@admin.site(Products)
class ProductsTable(admin.ModelAdmin):
    list_display = ['name', 'created']
    ordering = ['created']
