# Generated by Django 2.0.3 on 2018-04-28 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users_db_renote',
            old_name='lastname',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='users_db_renote',
            name='firstname',
        ),
    ]
