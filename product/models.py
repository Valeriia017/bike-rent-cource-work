from django.core.validators import FileExtensionValidator
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Назва")
    description = CKEditor5Field(blank=True, null=True, verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    image = models.ImageField(
        upload_to="images/",
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp"])
        ],
        null=True,
        blank=True,
        verbose_name="Зображення",
    )
    is_active = models.BooleanField(default=True, verbose_name="Активне")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"


class Place(models.Model):
    name = models.CharField(max_length=150, verbose_name="Адреса")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Місце"
        verbose_name_plural = "Місця"


class Order(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="Повне ім'я")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=150, verbose_name="Номер телефону")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Продукт"
    )
    enter_place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="enter_place",
        verbose_name="Місце отримання",
    )
    outer_place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="outer_place",
        verbose_name="Місце повернення",
    )
    ender_time = models.DateTimeField(
        verbose_name="Дата отримання",
    )
    outer_time = models.DateTimeField(
        verbose_name="Дата повернення",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Активне",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата створення",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата оновлення",
    )

    def __str__(self):
        return f"{self.id} {self.full_name}"

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"
