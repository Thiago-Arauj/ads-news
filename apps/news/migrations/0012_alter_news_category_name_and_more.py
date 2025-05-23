# Generated by Django 5.2.1 on 2025-05-11 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_merge_20250511_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category_name',
            field=models.CharField(choices=[('SCI', 'Ciencias'), ('BIS', 'Negócios'), ('WRL', 'Mundo'), ('HEL', 'Saúde'), ('TPN', 'Noticias de terceiros')], default='TPN', max_length=3, unique=True, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='thirdpartynews',
            name='category_name',
            field=models.CharField(choices=[('SCI', 'Ciencias'), ('BIS', 'Negócios'), ('WRL', 'Mundo'), ('HEL', 'Saúde'), ('TPN', 'Noticias de terceiros')], default='TPN', max_length=3, unique=True, verbose_name='Categoria'),
        ),
    ]
