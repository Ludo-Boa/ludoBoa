# Generated by Django 5.0.9 on 2024-11-11 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_myprofilesettings_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, verbose_name='titre')),
            ],
        ),
    ]
