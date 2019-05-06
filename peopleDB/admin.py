from django.contrib import admin
from .models import *




@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'rank_position',
        'position',
        'to_company',
        'to_vacancy',
        'step_recruit',
    )
    list_filter = ('to_company', 'date_add','step_recruit')
    search_fields = ('name',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'position',
        'link'

    )
    list_filter = ('city', 'position')
    search_fields = ('link',)

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Company)
admin.site.register(Vacancy)

