# Generated by Django 4.2.8 on 2024-02-18 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='forum.categories'),
        ),
    ]
