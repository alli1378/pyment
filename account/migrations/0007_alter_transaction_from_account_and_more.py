# Generated by Django 4.2.10 on 2024-02-11 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_savingaccount_checking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='from_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_user', to='account.checkingaccount'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='to_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_user', to='account.checkingaccount'),
        ),
    ]
