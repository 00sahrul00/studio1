# Generated by Django 5.0.3 on 2024-05-27 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photographer',
            name='specialization',
        ),
    ]
