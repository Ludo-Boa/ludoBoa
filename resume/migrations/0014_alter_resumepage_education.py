# Generated by Django 5.0.9 on 2024-12-07 22:56

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0013_alter_resumepage_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumepage',
            name='education',
            field=wagtail.fields.StreamField([('education_block', 9)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'form_classname': 'title', 'label': 'Titre', 'required': True}), 1: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('f9e300', 'Yellow'), ('2d72ff', 'DodgerBlue'), ('800080', 'Purple'), ('9574ce', 'MediumPurple'), ('0a753a', 'DarkGreen'), ('ee4d00 ', 'OrangeRed'), ('8aa9f9', 'LightSkyBlue'), ('8aa9f9', 'DeepPink')]}), 2: ('wagtail.blocks.CharBlock', (), {'form_classname': 'school', 'label': 'Ecole', 'required': True}), 3: ('wagtail.blocks.CharBlock', (), {'form_classname': 'city', 'label': 'Ville', 'required': True}), 4: ('wagtail.blocks.DateBlock', (), {'label': 'Date de début'}), 5: ('wagtail.blocks.DateBlock', (), {'label': 'Date de fin', 'required': False}), 6: ('wagtail.blocks.ChoiceBlock', [], {'blank': True, 'choices': [('', 'Selectionnez un niveau'), ('cap', 'CAP'), ('bep', 'BEP'), ('bac', 'BAC'), ('bac+2', 'BAC+2'), ('bac+3', 'BAC+3'), ('bac+4', 'BAC+4'), ('bac+5', 'BAC+5'), ('bac+8', 'BAC+8')], 'label': 'Niveau', 'required': False}), 7: ('wagtail.blocks.BooleanBlock', (), {'help_text': 'cocher la case si le diplôme a été obtenu', 'label': 'Diplôme', 'required': False}), 8: ('wagtail.blocks.RichTextBlock', (), {'features': ['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], 'icon': 'pilcrow', 'label': 'Description', 'required': False, 'template': 'blocks/paragraph_block.html'}), 9: ('wagtail.blocks.StructBlock', [[('title', 0), ('bg_color', 1), ('school', 2), ('city', 3), ('date_start', 4), ('date_end', 5), ('level', 6), ('certificate', 7), ('description', 8)]], {})}, verbose_name='formation'),
        ),
    ]
