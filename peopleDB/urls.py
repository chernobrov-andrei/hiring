from django.urls import path, include
from .views import list_view, dev_view, DevCreateView, MyDevCreateView, validate_username
from dal import autocomplete
from taggit.models import Tag

urlpatterns = [

    path('', list_view, name='list'),
    path('<int:id>/', dev_view, name='dev_view'),
    path('add/', DevCreateView.as_view(), name='dev_add'),
    path(
        'autocomplete/',
        autocomplete.Select2QuerySetView.as_view(
            queryset=Tag.objects.all(),
        ),
        name='select2_taggit',
    ),

    path('myform/', MyDevCreateView.as_view(), name='my_dev_add'),
    path('ajax/validate_username/', validate_username, name='validate_username'),

    path('select2/', include('django_select2.urls')),

]
