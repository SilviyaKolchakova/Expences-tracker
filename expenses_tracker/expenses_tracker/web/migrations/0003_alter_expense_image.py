# Generated by Django 3.2.12 on 2022-02-22 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_expense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='image',
            field=models.URLField(verbose_name='Link to Image'),
        ),
    ]
