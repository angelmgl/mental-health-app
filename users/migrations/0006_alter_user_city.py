# Generated by Django 5.0.2 on 2024-04-17 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_is_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=255, verbose_name='Ciudad donde vives'),
        ),
    ]
