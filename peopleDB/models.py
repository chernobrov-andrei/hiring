from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


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

    """Этап рекрутирования"""

    STEP_RECRUIT_CHOICES = {

        ('свободен', 'Свободен'),
        ('контакт', 'Контакт'),
        ('резюме отправлено', 'Резюме отправлено'),
        ('вакансия закрыта', 'Вакансия закрыта'),

    }

    recruit = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Имя разработчика", max_length=100, blank=True)
    country = models.ForeignKey(Country, verbose_name="Страна", on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, verbose_name="Город", on_delete=models.SET_NULL, null=True)
    rank_position = models.CharField("Уровень", max_length=20, choices=RANK_CHOICES, default='none')
    position = models.CharField("Должность", max_length=20, blank=True)
    skills = TaggableManager("Навыки")
    profile_link = models.URLField(null=True, blank=True)
    # resume =
    date_add = models.DateField('Дата добавления', auto_now_add=True)


    """Шаги рекрутинга"""

    step_recruit = models.CharField("Этап рекрутинга", max_length=40, choices=STEP_RECRUIT_CHOICES, default='свободен')

    class Meta:
        ordering = ['-date_add']

def __str__(self):
    return self.name


