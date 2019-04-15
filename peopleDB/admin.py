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


admin.site.register(Country)
admin.site.register(City)
admin.site.register(Company)
admin.site.register(Vacancy)

