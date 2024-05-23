from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import DetailView

from product.forms import OrderForm
from product.models import Product, Order


class OrderDetailView(DetailView):
    model = Order
    template_name = "pages/success-order.html"


def product_detail_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect("success-order", pk=order.id)
    else:
        form = OrderForm(initial={"product": product})
    context = {"product": product, "form": form}
    return render(request, "pages/product.html", context)
