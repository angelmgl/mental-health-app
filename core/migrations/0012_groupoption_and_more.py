# Generated by Django 5.0.2 on 2024-03-31 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_availabilityoption_option_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='professional',
            name='demographic_groups_served',
        ),
        migrations.AddField(
            model_name='professional',
            name='demographic_groups_served',
            field=models.ManyToManyField(related_name='professionals', to='core.groupoption'),
        ),
    ]
