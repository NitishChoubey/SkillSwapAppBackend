# Generated by Django 5.2.4 on 2025-07-22 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_user_is_staff_user_is_superuser"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProfileDetails",
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
                ("dob", models.DateField(blank=True, null=True)),
            ],
        ),
    ]
