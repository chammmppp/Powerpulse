# Generated by Django 5.0.7 on 2024-07-27 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_account_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(default='', max_length=128, unique=True),
        ),
    ]
