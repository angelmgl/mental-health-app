# Generated by Django 5.0.2 on 2024-03-29 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_availabilityoption_remove_professional_availability_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availabilityoption',
            name='option',
        ),
        migrations.AddField(
            model_name='availabilityoption',
            name='name',
            field=models.CharField(default='default', max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
