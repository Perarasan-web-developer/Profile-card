# Generated by Django 5.0.4 on 2024-05-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_kelvin_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='kelvin',
            name='owner',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='kelvin',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
