from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.documents import get_document_model

from base.blocks import ResumeStreamBlock, ExperienceStreamBlock



class resumePage(Page):
    intro = RichTextField(blank=True)
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="hero_image",
    )
    cv = models.ForeignKey(
        get_document_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    """
    Bloc Formation:
    ---------------
    Titre: champ texte
    Ecole: champ texte
    Ville: champ texte
    Date de début: champ date
    Date de fin: champ date
    Niveau: select
    Diplôme obtenu: case à cocher
    Description: champ texte enrichi
    """
    education = StreamField(
        ResumeStreamBlock(),
        verbose_name="formation",
        collapsed=True,
        blank=True,
        use_json_field=True,
    )

    """
    Bloc Expérience pro:
    Titre: champ texte
    Entreprise: champ texte
    Ville: champ texte
    Date de début: champ date
    Date de fin: champ date
    Description: champ texte enrichi
    """
    experience = StreamField(
        ExperienceStreamBlock(),
        verbose_name="expérience professionnelle",
        collapsed=True,
        blank=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('cv'),
        FieldPanel('hero_image'),
        FieldPanel('education'),
        FieldPanel('experience'),
    ]

    def __str__(self):
        return f"{self.title}"

    

   


