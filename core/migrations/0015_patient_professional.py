# Generated by Django 5.0.2 on 2024-04-09 23:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_cityoption_remove_professional_city_served_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='professional',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='core.professional'),
            preserve_default=False,
        ),
    ]
