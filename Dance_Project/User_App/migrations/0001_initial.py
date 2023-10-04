# Generated by Django 3.2.19 on 2023-10-04 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userAccountModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('personalinfo', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'userAccount_table',
            },
        ),
        migrations.CreateModel(
            name='userRolesModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roleName', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'userRoles_table',
            },
        ),
        migrations.CreateModel(
            name='userAccountRolesModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.ForeignKey(default=True, max_length=250, on_delete=django.db.models.deletion.CASCADE, related_name='userAccount', to='User_App.useraccountmodels')),
                ('userRoleId', models.ForeignKey(default=True, max_length=250, on_delete=django.db.models.deletion.CASCADE, related_name='userRoles', to='User_App.userrolesmodels')),
            ],
        ),
        migrations.CreateModel(
            name='directorModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_name', models.CharField(max_length=100)),
                ('director_contactInfo', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=200)),
                ('userId', models.ForeignKey(default=True, max_length=250, on_delete=django.db.models.deletion.CASCADE, related_name='director', to='User_App.useraccountmodels')),
            ],
            options={
                'db_table': 'dirtector_table',
            },
        ),
        migrations.CreateModel(
            name='coachModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coach_name', models.CharField(max_length=100)),
                ('coach_contactInfo', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=200)),
                ('userId', models.ForeignKey(default=True, max_length=250, on_delete=django.db.models.deletion.CASCADE, related_name='coach', to='User_App.useraccountmodels')),
            ],
            options={
                'db_table': 'coach_table',
            },
        ),
    ]
