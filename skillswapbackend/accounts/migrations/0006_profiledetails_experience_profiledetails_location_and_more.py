# Generated by Django 5.2.4 on 2025-07-24 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_profiledetails_occupation"),
    ]

    operations = [
        migrations.AddField(
            model_name="profiledetails",
            name="experience",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="profiledetails",
            name="location",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="profiledetails",
            name="skillowned",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
