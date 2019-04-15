# Generated by Django 2.1.5 on 2019-04-15 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('peopleDB', '0021_auto_20190415_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_company', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacancy', models.CharField(max_length=100)),
                ('name_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peopleDB.Company')),
            ],
        ),
        migrations.AlterField(
            model_name='developer',
            name='rank_position',
            field=models.CharField(choices=[('intern', 'Intern'), ('techlead', 'Tech Lead'), ('teamlead', 'Team Lead'), ('arch', 'Arch'), ('middle', 'Middle'), ('senior', 'Senior'), ('none', 'None'), ('junior', 'Junior')], default='none', max_length=20, verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='step_recruit',
            field=models.CharField(choices=[('none', 'None'), ('CV отправлено', 'CV отправлено')], default='none', max_length=20, verbose_name='В процессе'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='to_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='peopleDB.Company', verbose_name='В какую компанию'),
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.AddField(
            model_name='developer',
            name='to_vacancy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='peopleDB.Vacancy', verbose_name='На должность'),
        ),
    ]