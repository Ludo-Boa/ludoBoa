# Generated by Django 5.0.9 on 2024-11-10 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_myprofilesettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofilesettings',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='date de naissance'),
        ),
    ]
