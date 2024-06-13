# Generated by Django 5.0.6 on 2024-06-13 17:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='review',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='author', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='is_bestselling',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.IntegerField(default=8, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
            preserve_default=False,
        ),
    ]