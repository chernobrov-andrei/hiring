# Generated by Django 2.1.5 on 2019-03-26 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peopleDB', '0014_auto_20190212_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='job_opotunity',
            field=models.CharField(choices=[('не ищет работу', 'Не ищет работу'), ('возможно ищет работу', 'Возможно ищет работу')], default='возможно ищет работу', max_length=40, verbose_name='Ищет или нет'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='rank_position',
            field=models.CharField(choices=[('teamlead', 'Team Lead'), ('techlead', 'Tech Lead'), ('none', 'None'), ('arch', 'Arch'), ('intern', 'Intern'), ('junior', 'Junior'), ('senior', 'Senior'), ('middle', 'Middle')], default='none', max_length=20, verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='step_recruit',
            field=models.CharField(choices=[('в контактах', 'В контактак'), ('запрос на добавление', 'Запрос на добавление'), ('свободен', 'Свободен')], default='свободен', max_length=40, verbose_name='Этап рекрутинга'),
        ),
    ]
