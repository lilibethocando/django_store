from django.contrib import admin
from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "unit_price", "collection"]
    list_editable = ["unit_price"]
    list_per_page = 10
    list_select_related = ["collection"]

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "products_count"]
    list_per_page = 10

    def products_count(self, collection):
        return collection.product_set.count()

    products_count.short_description = "Number of products"

@admin.register(models.Customer)
class Customer(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership"]
    list_editable = ["membership"]
    list_per_page = 10


@admin.register(models.Order)
class Order(admin.ModelAdmin):
    list_display = ["id", "placed_at", "customer"]
    list_per_page = 10
    list_select_related = ["customer"]