from .models import Developer
import django_filters
from django import forms


class DeveloperFilter(django_filters.FilterSet):

    class Meta:
        model = Developer
        fields = ['country', 'city', 'rank_position', 'position','step_recruit',]