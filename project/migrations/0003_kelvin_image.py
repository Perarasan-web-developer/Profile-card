# Generated by Django 5.0.4 on 2024-04-23 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_tag_kelvin_vote_ratio_kelvin_vote_total_review_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kelvin',
            name='image',
            field=models.ImageField(blank=True, default='default_image.jpg', null=True, upload_to=''),
        ),
    ]