from django.contrib import admin
from django.utils.html import format_html

from product.models import Product, Place, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ("-created_at",)
    list_display_links = ("id", "display_image", "name")
    list_display = (
        "id",
        "display_image",
        "name",
        "is_active",
        "created_at",
        "updated_at",
    )
    search_fields = ("id", "name", "description")
    list_filter = ("is_active", "created_at", "updated_at")

    @admin.display(description="Зображення")
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="100" />', obj.image.url)
        else:
            return "No Image"


@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    ordering = ("-created_at",)
    list_display_links = ("id", "full_name")
    list_display = (
        "id",
        "full_name",
        "product",
        "created_at",
        "enter_place",
        "ender_time",
        "is_active",
    )
    search_fields = ("full_name", "product__name", "id")
    list_filter = ("enter_place", "ender_time", "is_active")


admin.site.register(Place)
