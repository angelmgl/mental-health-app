# Generated by Django 5.0.2 on 2024-04-10 00:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_patient_professional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='professional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='core.professional'),
        ),
    ]
