# Generated by Django 2.0.3 on 2018-04-14 18:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note_Db_Renote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_code', models.CharField(max_length=60, unique=True)),
                ('count', models.FloatField(default=0)),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('photo', models.FileField(upload_to='upload')),
                ('Tr_group', models.CharField(blank=True, default='', max_length=100)),
                ('Tr_hashtag', models.CharField(blank=True, default='', max_length=90)),
                ('description', models.CharField(blank=True, default='', max_length=5000)),
                ('weekday_name', models.CharField(blank=True, default='', max_length=100)),
                ('payment_method', models.CharField(blank=True, default='', max_length=40)),
                ('cost', models.FloatField(blank=True, default='', max_length=40)),
                ('celery_task_id', models.CharField(blank=True, default='', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users_Db_Renote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=40)),
                ('user_email', models.EmailField(blank=True, default='', max_length=160)),
                ('user_pass', models.CharField(default='', max_length=50)),
                ('firstname', models.CharField(blank=True, default='', max_length=40)),
                ('lastname', models.CharField(blank=True, default='', max_length=80)),
                ('status', models.CharField(blank=True, default='', max_length=40)),
                ('isverified', models.IntegerField(blank=True, default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('photo', models.FileField(upload_to='upload')),
                ('firebase_notif_ID', models.CharField(blank=True, default='', max_length=10000)),
                ('onesignal_notif_ID', models.CharField(blank=True, default='', max_length=10000)),
                ('devices_types_list', models.CharField(blank=True, default='', max_length=500)),
                ('devices_id_list', models.CharField(blank=True, default='', max_length=15000)),
                ('devices_last_login_times', models.CharField(blank=True, default='', max_length=2500)),
                ('last_login_time', models.CharField(blank=True, default='', max_length=2500)),
                ('assigned_token', models.CharField(blank=True, default='', max_length=1500)),
                ('assigned_token_stamps', models.DateTimeField(blank=True, default='1900-01-01 10:10', null=True)),
                ('confirm_sms_val', models.CharField(blank=True, max_length=10)),
                ('confirm_sms_time_stamp', models.DateTimeField(blank=True, default='1900-01-01 10:10', null=True)),
                ('user_credit', models.FloatField(blank=True, default=0)),
                ('is_black', models.BooleanField(default=0)),
                ('introduction_code', models.CharField(blank=True, default='', max_length=20)),
                ('who_introduction_code', models.CharField(blank=True, default='', max_length=20)),
                ('state', models.CharField(blank=True, default='', max_length=90)),
                ('city', models.CharField(blank=True, default='', max_length=90)),
                ('mount_cost', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Users_Tokens_Db_Renote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_token', models.CharField(max_length=60, unique=True)),
                ('assigned_token_stamps', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('assigned_token_last_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('device', models.CharField(blank=True, default='', max_length=100)),
                ('celery_task_id', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Users_Db_Renote')),
            ],
        ),
        migrations.AddField(
            model_name='Note_Db_Renote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Users_Db_Renote'),
        ),
    ]
