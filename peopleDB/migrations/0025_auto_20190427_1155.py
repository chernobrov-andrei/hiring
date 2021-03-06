# Generated by Django 2.1.5 on 2019-04-27 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('peopleDB', '0024_auto_20190427_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dolgnost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='peopleDB.Position'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='rank_position',
            field=models.CharField(choices=[('intern', 'Intern'), ('techlead', 'Tech Lead'), ('junior', 'Junior'), ('teamlead', 'Team Lead'), ('arch', 'Arch'), ('senior', 'Senior'), ('middle', 'Middle'), ('none', 'None')], default='none', max_length=20, verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='step_recruit',
            field=models.CharField(choices=[('none', 'None'), ('CV отправлено', 'CV отправлено')], default='none', max_length=20, verbose_name='В процессе'),
        ),
    ]
