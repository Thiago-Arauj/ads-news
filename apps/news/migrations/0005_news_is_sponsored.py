# Generated by Django 5.2.1 on 2025-05-10 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='is_sponsored',
            field=models.BooleanField(default=False, verbose_name='Patrocinada'),
        ),
    ]
