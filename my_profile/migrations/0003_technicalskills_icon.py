# Generated by Django 4.2.5 on 2023-10-07 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0002_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='technicalskills',
            name='icon',
            field=models.CharField(blank=True, help_text="Nom de l'icone sur Devicon", max_length=50, verbose_name='icone'),
        ),
    ]
