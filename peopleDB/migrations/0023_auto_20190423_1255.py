# Generated by Django 2.1.5 on 2019-04-23 12:55

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('peopleDB', '0022_auto_20190415_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Имя разработчика')),
                ('position', models.CharField(blank=True, max_length=200, verbose_name='Должность')),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('date_add', models.DateField(auto_now_add=True, verbose_name='Дата добавления')),
                ('skills', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Навыки')),
            ],
        ),
        migrations.AlterModelOptions(
            name='developer',
            options={},
        ),
        migrations.AlterField(
            model_name='developer',
            name='rank_position',
            field=models.CharField(choices=[('intern', 'Intern'), ('junior', 'Junior'), ('middle', 'Middle'), ('techlead', 'Tech Lead'), ('arch', 'Arch'), ('none', 'None'), ('teamlead', 'Team Lead'), ('senior', 'Senior')], default='none', max_length=20, verbose_name='Уровень'),
        ),
    ]
