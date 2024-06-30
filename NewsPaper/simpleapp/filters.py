from django_filters import FilterSet

from .models import Products, Post


class ProductFilter(FilterSet):
    class Meta:
        model = Products
        fields = {
            'productsmaterial__material' : ['exact'],
            'name': ['icontains'],
            'quantity' : ['gt'],
            'price': ['lt','gt'],
        }


