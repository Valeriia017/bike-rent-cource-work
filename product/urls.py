from django.urls import path
from django.views.generic import TemplateView

from . import views
from .views import OrderDetailView

urlpatterns = [
    path("<int:pk>/", views.product_detail_view, name="product-detail"),
    path(
        "success-order/<int:pk>",
        OrderDetailView.as_view(),
        name="success-order",
    ),
    path(
        "success-closed/",
        TemplateView.as_view(),
        name="success-closed",
    ),
]
