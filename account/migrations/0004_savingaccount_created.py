# Generated by Django 4.2.10 on 2024-02-11 13:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_checking_checkingaccount_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='savingaccount',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
