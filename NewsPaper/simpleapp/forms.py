from django import forms
from django.core.exceptions import ValidationError

from .models import Products, Post


class ProductsForm(forms.ModelForm):
    description = forms.CharField(min_length=20)
    class Meta:
        model = Products
        fields = [
            'name',
            'description',
            'category',
            'price',
            'quantity',
        ]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'categories',
            'post_type',
            'text',
            'title',
        ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("name")
        title = cleaned_data.get("title")

        if text == title:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )
        return cleaned_data