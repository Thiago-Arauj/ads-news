# Generated by Django 5.2.1 on 2025-05-10 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_category_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='color',
            field=models.CharField(default='#000000', max_length=7, verbose_name='Cor'),
        ),
    ]
