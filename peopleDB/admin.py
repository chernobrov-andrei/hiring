from django.contrib import admin
from .models import *

class DeveloperAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'rank_position',
        'position',
        'step_recruit',
        'job_opotunity',
    )
    list_filter = ('rank_position', 'position', 'step_recruit', 'date_add', 'job_opotunity',)
    search_fields = ('name',)




admin.site.register(Developer,DeveloperAdmin)
admin.site.register(Country)
admin.site.register(City)
