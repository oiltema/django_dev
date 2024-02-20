# Generated by Django 4.2.8 on 2024-02-16 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_post_date_create_post_date_update_post_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
