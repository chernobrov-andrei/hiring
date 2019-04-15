from django import forms
from .models import Developer
from dal import autocomplete


class DevForm(forms.ModelForm):

     class Meta:
        model = Developer
        fields = ('name', 'profile_link', 'country', 'city', 'rank_position', 'position', 'skills', 'comment',)
        widgets = {
            'skills': autocomplete.TaggitSelect2('select2_taggit'),
            'name': forms.TextInput(attrs={'placeholder': 'Введите имя'})
        }


class MyForm(forms.ModelForm):
    class Meta:
        model = Developer

        fields = ('name', 'country', 'city', 'rank_position', 'position', 'skills', 'profile_link',)

