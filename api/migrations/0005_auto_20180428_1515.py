# Generated by Django 2.0.3 on 2018-04-28 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_like'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Like',
            new_name='Likes_DB',
        ),
    ]
