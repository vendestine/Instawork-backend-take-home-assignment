# Generated by Django 4.1.3 on 2022-11-16 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                ("userId", models.IntegerField(primary_key=True, serialize=False)),
                ("firstName", models.CharField(default="", max_length=100)),
                ("lastName", models.CharField(default="", max_length=100)),
                ("phone", models.CharField(default="", max_length=45)),
                ("emailId", models.CharField(default="", max_length=200)),
                (
                    "role",
                    models.CharField(
                        choices=[("admin", "Admin"), ("regular", "Regular")],
                        default="regular",
                        max_length=45,
                    ),
                ),
            ],
        ),
    ]