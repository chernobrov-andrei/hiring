from django.contrib import admin
from .models import *

class DeveloperAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'rank_position',
        'position',
        'recruit',
        'step_recruit'
    )
    list_filter = ('rank_position', 'position', 'step_recruit', 'date_add',)
    search_fields = ('name',)




admin.site.register(Developer,DeveloperAdmin)
admin.site.register(Country)
admin.site.register(City)
