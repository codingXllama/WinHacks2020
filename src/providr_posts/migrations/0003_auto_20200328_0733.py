# Generated by Django 3.0 on 2020-03-28 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providr_posts', '0002_userpost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
