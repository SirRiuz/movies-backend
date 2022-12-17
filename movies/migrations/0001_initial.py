# Generated by Django 4.1.4 on 2022-12-15 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                (
                    "name",
                    models.CharField(
                        default=None,
                        help_text="Name of the move",
                        max_length=1000,
                        null=None,
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        default=None,
                        help_text="Gender of the move",
                        max_length=1000,
                        null=None,
                    ),
                ),
                ("isMove", models.BooleanField(default=True)),
                (
                    "views",
                    models.IntegerField(
                        default=None, help_text="Number of the views", null=None
                    ),
                ),
                (
                    "score",
                    models.IntegerField(
                        default=None, help_text="Name of the score", null=None
                    ),
                ),
            ],
        ),
    ]