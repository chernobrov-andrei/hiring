from django.urls import path, include
from .views import list_view, DevCreateView, validate_username
from dal import autocomplete
from taggit.models import Tag

urlpatterns = [

    path('', list_view, name='list'),
    path('add/', DevCreateView.as_view(), name='dev_add'),
    path(
        'autocomplete/',
        autocomplete.Select2QuerySetView.as_view(
            queryset=Tag.objects.all(),
        ),
        name='select2_taggit',
    ),

    path('ajax/validate_username/', validate_username, name='validate_username'),

    path('select2/', include('django_select2.urls')),

]
