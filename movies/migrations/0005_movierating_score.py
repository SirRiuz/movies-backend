# Generated by Django 4.1.4 on 2022-12-15 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0004_movierating"),
    ]

    operations = [
        migrations.AddField(
            model_name="movierating",
            name="score",
            field=models.IntegerField(default=0),
        ),
    ]