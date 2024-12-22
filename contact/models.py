from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PublishingPanel,
)
from wagtail.admin.panels import TabbedInterface, TitleFieldPanel, ObjectList

from wagtail.fields import RichTextField
from wagtail.models import (
    Page,
    DraftStateMixin,
    PreviewableMixin,
    RevisionMixin,
    TranslatableMixin,
)

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)
from wagtail.snippets.models import register_snippet
from django.forms import widgets 




class FormField(AbstractFormField):
    page = ParentalKey('ContactPage', on_delete=models.CASCADE, related_name='form_fields')


class ContactPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Hero image",
    )

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro'),
        InlinePanel('form_fields', label="Champ de formulaire"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    banner_panels = [
        FieldPanel('hero_image'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Contenu'),
        ObjectList(banner_panels, heading='Bannière'),
        ObjectList(Page.promote_panels, heading='Promotion'),
    ])

    

    
