from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Company(models.Model):
    """Название компании куда ищим разроба"""
    name_company = models.CharField(max_length=100)

    def __str__(self):
        return self.name_company

class Vacancy(models.Model):
    """Вакансия"""
    name_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    vacancy = models.CharField(max_length=100)

    def __str__(self):
        return self.vacancy


class Country(models.Model):
    """Страна"""
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class City(models.Model):
    """Город"""
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Developer(models.Model):
    """Уровень разроба"""

    RANK_CHOICES = {
        ('none', 'None'),
        ('intern', 'Intern'),
        ('junior', 'Junior'),
        ('middle', 'Middle'),
        ('senior', 'Senior'),
        ('teamlead', 'Team Lead'),
        ('techlead', 'Tech Lead'),
        ('arch', 'Arch'),

    }

    STEP_CHOICES = {
        ('none', 'None'),
        ('CV отправлено', 'CV отправлено'),


    }

    recruit = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Имя разработчика", max_length=100, blank=True)
    profile_link = models.URLField(null=True, blank=True)
    country = models.ForeignKey(Country, verbose_name="Страна", on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, verbose_name="Город", on_delete=models.SET_NULL, null=True)
    rank_position = models.CharField("Уровень", max_length=20, choices=RANK_CHOICES, default='none')
    position = models.CharField("Должность", max_length=20, blank=True)
    skills = TaggableManager("Навыки")
    comment = models.TextField("Комментарий", blank=True)
    date_add = models.DateField('Дата добавления', auto_now_add=True)

    to_company = models.ForeignKey(Company, verbose_name="В какую компанию", on_delete=models.SET_NULL, null=True, blank=True)
    to_vacancy = models.ForeignKey(Vacancy, verbose_name="На должность", on_delete=models.SET_NULL, null=True, blank=True)
    step_recruit = models.CharField("В процессе", max_length=20, choices=STEP_CHOICES, default='none')


    class Meta:
        ordering = ['-date_add']

def __str__(self):
    return self.name


