from .models import Developer
from taggit.models import Tag
import django_filters
from django import forms
from django_select2.forms import *



class DeveloperFilter(django_filters.FilterSet):
    skills_first = django_filters.ModelChoiceFilter(field_name='skills', queryset=Developer.skills.all())
    skills_second = django_filters.ModelChoiceFilter(field_name='skills', queryset=Developer.skills.all())
    skills_thed = django_filters.ModelChoiceFilter(field_name='skills', queryset=Developer.skills.all())

    class Meta:
        model = Developer
        fields = ['city', 'position', 'rank_position', 'skills_first', 'skills_second', 'skills_thed',]

