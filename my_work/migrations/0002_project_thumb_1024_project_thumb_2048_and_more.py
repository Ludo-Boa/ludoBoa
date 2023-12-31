# Generated by Django 4.2.5 on 2023-10-21 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_work', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='thumb_1024',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='thumb_2048',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='thumb_256',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='thumb_512',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='', upload_to='projects/images'),
        ),
    ]
