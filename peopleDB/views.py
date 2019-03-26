from django.shortcuts import render, redirect
from .filters import DeveloperFilter
from .models import Developer
from .forms import StepRecruit, DevForm, MyForm
from django.views.generic import CreateView, UpdateView
from django.http import JsonResponse



def validate_username(request):
    name = request.GET.get('name', None)
    data = {
        'is_taken': Developer.objects.filter(name__iexact=name).exists()
    }
    return JsonResponse(data)




class DevCreateView(CreateView):
    model = Developer
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



class MyDevCreateView(CreateView):
    model = Developer
    form_class = MyForm

    def form_valid(self, form):
        """Автоматическое добавление пользователя"""
        object = form.save(commit=False)
        object.recruit = self.request.user
        object.save()
        form.save_m2m()
        return redirect("my_dev_add")

    def success_url(self):
        return redirect("my_dev_add")






def list_view(request):
    user_list = Developer.objects.all()
    user_filter = DeveloperFilter(request.GET, queryset=user_list)
    form = StepRecruit()

    context = dict(filter=user_filter, list=user_list, step=form)
    return render(request, 'peopleDB/filter/list.html', context)



def dev_view(request, id):
    dev = Developer.objects.get(id=id)

    context = {
        'dev': dev,

    }
    return render(request, 'peopleDB/detail/dev_detail.html', context)