# Generated by Django 5.1 on 2024-09-10 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0002_rename_membership_membership_model'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='membership_model',
            options={'ordering': ['name'], 'verbose_name_plural': 'Gym Members'},
        ),
    ]
