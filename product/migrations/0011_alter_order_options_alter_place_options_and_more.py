# Generated by Django 5.0.6 on 2024-05-23 05:05

import django.core.validators
import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0010_alter_order_email_alter_order_full_name_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={"verbose_name": "Замовлення", "verbose_name_plural": "Замовлення"},
        ),
        migrations.AlterModelOptions(
            name="place",
            options={"verbose_name": "Місце", "verbose_name_plural": "Місця"},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "Продукт", "verbose_name_plural": "Продукти"},
        ),
        migrations.AlterField(
            model_name="order",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Дата створення"
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="email",
            field=models.EmailField(max_length=254, verbose_name="Email"),
        ),
        migrations.AlterField(
            model_name="order",
            name="ender_time",
            field=models.DateTimeField(verbose_name="Дата отримання"),
        ),
        migrations.AlterField(
            model_name="order",
            name="enter_place",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="enter_place",
                to="product.place",
                verbose_name="Місце отримання",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="full_name",
            field=models.CharField(max_length=150, verbose_name="Повне ім'я"),
        ),
        migrations.AlterField(
            model_name="order",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Активне"),
        ),
        migrations.AlterField(
            model_name="order",
            name="outer_place",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="outer_place",
                to="product.place",
                verbose_name="Місце повернення",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="outer_time",
            field=models.DateTimeField(verbose_name="Дата повернення"),
        ),
        migrations.AlterField(
            model_name="order",
            name="phone",
            field=models.CharField(max_length=150, verbose_name="Номер телефону"),
        ),
        migrations.AlterField(
            model_name="order",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="product.product",
                verbose_name="Продукт",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Дата оновлення"),
        ),
        migrations.AlterField(
            model_name="place",
            name="name",
            field=models.CharField(max_length=150, verbose_name="Адреса"),
        ),
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Дата створення"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True, null=True, verbose_name="Опис"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="images/",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["jpg", "jpeg", "png", "webp"]
                    )
                ],
                verbose_name="Зображення",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Активне"),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=150, verbose_name="Назва"),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Ціна"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Дата оновлення"),
        ),
    ]
