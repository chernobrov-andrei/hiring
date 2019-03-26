from django import template
from peopleDB.models import Developer

register = template.Library()

@register.simple_tag
def total_dev():
    return Developer.objects.all().count()