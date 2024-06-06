# Generated by Django 5.0.4 on 2024-05-11 04:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_kelvin_owner_alter_kelvin_title'),
        ('users', '0008_alter_inbox_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kelvin',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]
