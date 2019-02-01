# Generated by Django 2.1.5 on 2019-02-01 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peopleDB', '0005_auto_20190201_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='rank_position',
            field=models.CharField(choices=[('middle', 'Middle'), ('teamlead', 'Team Lead'), ('senior', 'Senior'), ('techlead', 'Tech Lead'), ('junior', 'Junior'), ('none', 'None'), ('intern', 'Intern'), ('arch', 'Arch')], default='none', max_length=20, verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='step_recruit',
            field=models.CharField(choices=[('контакт', 'Контакт'), ('резюме отправлено', 'Резюме отправлено'), ('вакансия закрыта', 'Вакансия закрыта'), ('свободен', 'Свободен')], default='свободен', max_length=40, verbose_name='Этап рекрутинга'),
        ),
    ]