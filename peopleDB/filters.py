from .models import Profile
from taggit.models import Tag
import django_filters



class DeveloperFilter(django_filters.FilterSet):
    city = django_filters.AllValuesMultipleFilter()
    skills = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all())
    position = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Profile
        fields = []
