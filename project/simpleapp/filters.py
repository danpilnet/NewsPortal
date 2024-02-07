from django import forms
from django_filters import FilterSet, DateFilter
from .models import Post


class PostFilter(FilterSet):
    post_time = DateFilter(widget=forms.DateInput(attrs={'type': 'date'}),
                           label='Дата',
                           lookup_expr='date__gte')

    class Meta:
        model = Post
        fields = {
            'text': ['icontains', ],
        }
