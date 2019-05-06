# Generated by Django 2.1.5 on 2019-04-27 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peopleDB', '0025_auto_20190427_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='dolgnost',
        ),
        migrations.AlterField(
            model_name='developer',
            name='rank_position',
            field=models.CharField(choices=[('junior', 'Junior'), ('techlead', 'Tech Lead'), ('senior', 'Senior'), ('teamlead', 'Team Lead'), ('intern', 'Intern'), ('middle', 'Middle'), ('none', 'None'), ('arch', 'Arch')], default='none', max_length=20, verbose_name='Уровень'),
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]