# Generated by Django 4.1.3 on 2023-01-17 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0002_goalcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления'),
        ),
        migrations.AlterField(
            model_name='goalcategory',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='goalcategory',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления'),
        ),
        migrations.AlterField(
            model_name='goalcomment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='goalcomment',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления'),
        ),
    ]