from django.shortcuts import render, redirect
from .filters import DeveloperFilter
from .models import Profile, Developer
from taggit.models import Tag
from .forms import DevForm
from django.views.generic import CreateView
from django.http import JsonResponse



def validate_username(request):
    name = request.GET.get('name', None)
    data = {
        'is_taken': Profile.objects.filter(name__iexact=name).exists()
    }
    return JsonResponse(data)




class DevCreateView(CreateView):
    model = Profile
    form_class = DevForm

    def form_valid(self, form):
        """Автоматическое добавление пользователя"""
        object = form.save(commit=False)
        object.recruit = self.request.user
        object.save()
        form.save_m2m()
        return redirect("dev_add")

    def success_url(self):
        return redirect("dev_add")


def list_view(request):
    user_list = Profile.objects.all()
    user_filter = DeveloperFilter(request.GET, queryset=user_list)

    context = dict(filter=user_filter, list=user_list)
    return render(request, 'peopleDB/filter/list.html', context)

