# Generated by Django 4.2.8 on 2024-02-16 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_post_simple'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='simple',
        ),
    ]
