from django import template
from peopleDB.models import Profile

register = template.Library()

@register.simple_tag
def total_dev():
    return Profile.objects.all().count()