# Generated by Django 2.0.3 on 2018-05-04 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20180503_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow_db',
            name='request',
        ),
        migrations.AddField(
            model_name='follow_db',
            name='accepted',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='users_db_renote',
            name='private',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
