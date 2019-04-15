# Generated by Django 2.1.5 on 2019-03-27 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peopleDB', '0015_auto_20190326_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='job_opotunity',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='step_recruit',
        ),
        migrations.AlterField(
            model_name='developer',
            name='rank_position',
            field=models.CharField(choices=[('senior', 'Senior'), ('junior', 'Junior'), ('middle', 'Middle'), ('intern', 'Intern'), ('arch', 'Arch'), ('none', 'None'), ('teamlead', 'Team Lead'), ('techlead', 'Tech Lead')], default='none', max_length=20, verbose_name='Уровень'),
        ),
    ]
