# Generated by Django 3.2.11 on 2022-01-13 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0003_alter_gamelog_log_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='move',
            name='result',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
