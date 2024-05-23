from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Order


class PreOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["product", "enter_place", "outer_place", "ender_time", "outer_time"]
        widgets = {
            "ender_time": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form__element"}
            ),
            "outer_time": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form__element"}
            ),
        }
        labels = {
            "product": "Продукт",
            "enter_place": "Місце отримання",
            "outer_place": "Місце повернення",
            "ender_time": "Дата отримання",
            "outer_time": "Дата повернення",
        }

    def clean(self):
        cleaned_data = super().clean()
        in_place_time = cleaned_data.get("in_place_time")
        out_place_time = cleaned_data.get("out_place_time")

        if in_place_time and out_place_time and out_place_time < in_place_time:
            raise ValidationError("Дата повернення не може бути раніше дати отримання")

        return cleaned_data


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "full_name",
            "email",
            "phone",
            "product",
            "enter_place",
            "outer_place",
            "ender_time",
            "outer_time",
        ]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Ваше повне ім'я"}),
            "email": forms.EmailInput(attrs={"placeholder": "Ваша електронна пошта"}),
            "phone": forms.TextInput(attrs={"placeholder": "Ваш номер телефону"}),
            "ender_time": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form__element"}
            ),
            "outer_time": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form__element"}
            ),
        }
        labels = {
            "full_name": _("Повне ім'я"),
            "email": _("Електронна пошта"),
            "phone": _("Телефон"),
            "product": _("Продукт"),
            "enter_place": _("Місце отримання"),
            "outer_place": _("Місце повернення"),
            "ender_time": _("Дата отримання"),
            "outer_time": _("Дата повернення"),
        }

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")
        if " " not in full_name:
            raise forms.ValidationError(_("Введіть повне ім'я"))
        return full_name

    def clean(self):
        cleaned_data = super().clean()
        ender_time = cleaned_data.get("ender_time")
        outer_time = cleaned_data.get("outer_time")

        if ender_time and outer_time and outer_time < ender_time:
            raise forms.ValidationError(
                _("Дата повернення не може бути раніше дати отримання")
            )

        return cleaned_data
