# Generated by Django 3.2.4 on 2021-06-08 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatting', '0003_rename_individual_chart_chat_individual_chat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='status',
            name='contact',
        ),
        migrations.AddField(
            model_name='settings',
            name='about',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='settings',
            name='mobile_no',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='settings',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='settings',
            name='profile_pic',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='call',
            name='contact',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
