from django import forms
from .models import Developer
from dal import autocomplete


class StepRecruit(forms.ModelForm):

    class Meta:
        model = Developer
        fields = ('step_recruit',)



class DevForm(forms.ModelForm):
     class Meta:
        model = Developer
        fields = ('name', 'country', 'city', 'rank_position', 'position', 'skills', 'profile_link',)
        widgets = {
            'skills': autocomplete.TaggitSelect2('select2_taggit')
        }


class MyForm(forms.ModelForm):
    class Meta:
        model = Developer

        fields = ('name', 'country', 'city', 'rank_position', 'position', 'skills', 'profile_link',)
