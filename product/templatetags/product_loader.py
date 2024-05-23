from django import template

from product.models import Product

register = template.Library()


@register.simple_tag()
def get_active_products() -> list[Product]:
    active_products = Product.objects.filter(is_active=True).all()
    return active_products
