# Generated by Django 5.0.9 on 2024-11-09 09:10

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumepage',
            name='education',
            field=wagtail.fields.StreamField([('title', 0), ('school', 1), ('city', 2), ('date_start', 3), ('date_end', 3), ('level', 4), ('certificate', 5), ('description', 6)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'form_classname': 'title', 'required': True}), 1: ('wagtail.blocks.CharBlock', (), {'form_classname': 'school', 'required': True}), 2: ('wagtail.blocks.CharBlock', (), {'form_classname': 'city', 'required': True}), 3: ('wagtail.blocks.DateBlock', (), {}), 4: ('wagtail.blocks.ChoiceBlock', [], {'blank': True, 'choices': [('', 'Select a level'), ('cap', 'CAP'), ('bep', 'BEP'), ('bac', 'BAC'), ('bac+2', 'BAC+2'), ('bac+3', 'BAC+3'), ('bac+4', 'BAC+4'), ('bac+5', 'BAC+5'), ('bac+8', 'BAC+8')], 'required': False}), 5: ('wagtail.blocks.BooleanBlock', (), {}), 6: ('wagtail.blocks.RichTextBlock', (), {'features': ['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], 'icon': 'pilcrow', 'template': 'blocks/paragraph_block.html'})}, verbose_name='Bloc de formation'),
        ),
    ]