# Generated by Django 4.2.10 on 2024-02-11 12:03

import account.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckingAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SavingAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('exp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', account.models.IntegerRangeField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('from_account', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_user', to='account.checkingaccount')),
                ('to_account', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_user', to='account.checkingaccount')),
            ],
        ),
    ]
