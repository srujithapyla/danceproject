# Generated by Django 4.1.10 on 2023-09-14 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ageGroupModels",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ageRange", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "ageGroup_table",
            },
        ),
        migrations.CreateModel(
            name="artistModels",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("personalinfo", models.CharField(max_length=200)),
                (
                    "ageGroupid",
                    models.ForeignKey(
                        default=True,
                        max_length=250,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="age_group",
                        to="Dance_App.agegroupmodels",
                    ),
                ),
            ],
            options={
                "db_table": "artist_table",
            },
        ),
        migrations.CreateModel(
            name="performanceModels",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField()),
                ("location", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=500)),
                (
                    "artistId",
                    models.ForeignKey(
                        default=True,
                        max_length=250,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="performance",
                        to="Dance_App.artistmodels",
                    ),
                ),
            ],
            options={
                "db_table": "Performance_table",
            },
        ),
        migrations.CreateModel(
            name="injuryRecordModels",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField()),
                ("injuryDescription", models.CharField(max_length=500)),
                (
                    "artistId",
                    models.ForeignKey(
                        default=True,
                        max_length=250,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="injuryRecord",
                        to="Dance_App.artistmodels",
                    ),
                ),
            ],
            options={
                "db_table": "injuryRecord_table",
            },
        ),
        migrations.CreateModel(
            name="clubActivitiesModels",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("activityName", models.CharField(max_length=100)),
                ("date", models.DateTimeField()),
                ("description", models.CharField(max_length=500)),
                (
                    "artistId",
                    models.ForeignKey(
                        default=True,
                        max_length=250,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="clubActivities",
                        to="Dance_App.artistmodels",
                    ),
                ),
            ],
            options={
                "db_table": "clubActivities_table",
            },
        ),
        migrations.CreateModel(
            name="attendanceRecordModels",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField()),
                ("status", models.CharField(max_length=100)),
                (
                    "artistId",
                    models.ForeignKey(
                        default=True,
                        max_length=250,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attendanceRecord",
                        to="Dance_App.artistmodels",
                    ),
                ),
            ],
            options={
                "db_table": "attendanceRecord_table",
            },
        ),
    ]
