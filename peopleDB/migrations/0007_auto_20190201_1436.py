# Generated by Django 2.1.5 on 2019-02-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peopleDB', '0006_auto_20190201_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='rank_position',
            field=models.CharField(choices=[('techlead', 'Tech Lead'), ('none', 'None'), ('senior', 'Senior'), ('junior', 'Junior'), ('arch', 'Arch'), ('intern', 'Intern'), ('teamlead', 'Team Lead'), ('middle', 'Middle')], default='none', max_length=20, verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='step_recruit',
            field=models.CharField(choices=[('вакансия закрыта', 'Вакансия закрыта'), ('резюме отправлено', 'Резюме отправлено'), ('свободен', 'Свободен'), ('контакт', 'Контакт')], default='свободен', max_length=40, verbose_name='Этап рекрутинга'),
        ),
    ]