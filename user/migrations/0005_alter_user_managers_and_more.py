# Generated by Django 4.1 on 2022-08-28 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_user_username"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[],
        ),
        migrations.RenameField(
            model_name="follower",
            old_name="profile_uuid",
            new_name="profile",
        ),
        migrations.RenameField(
            model_name="follower",
            old_name="user_uuid",
            new_name="user",
        ),
    ]
