# Generated by Django 5.2.4 on 2025-07-25 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0009_alter_profiledetails_experience"),
    ]

    operations = [
        migrations.AddField(
            model_name="profiledetails",
            name="profile_picture",
            field=models.ImageField(blank=True, null=True, upload_to="profile_pics/"),
        ),
    ]
