from django import forms
from django.db import models
from wagtail.models import Page
from wagtail.search import index
from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, HelpPanel
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.snippets.models import register_snippet



class PortfolioIndexPage(Page):
    body = RichTextField(blank=True)
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Page Hero image",
    )

    def get_context(self, request):
        # Mettre à jour le contexte pour inclure uniquement les publications publiées, classées par ordre chronologique inverse
        context = super().get_context(request)
        project_list = self.get_children().live().order_by('-first_published_at')
        context['project_list'] = project_list
        project_categories = PortfolioCategory.objects.all()
        context['project_categories'] = project_categories
        return context

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('hero_image'),
    ]



class PortfolioPage(Page):
    created = models.DateField("date de création", blank=True)
    description = RichTextField(blank=True)
    link = models.URLField("lien du projet", max_length=255, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Image du projet",
    )
    category = models.ForeignKey(
        "portfolio.PortfolioCategory", 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Catégorie du projet",
    )

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('description'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('created'),
        FieldPanel('description'),
        FieldPanel('link'),
        FieldPanel('image'),
        FieldPanel("category", widget=forms.RadioSelect),
        
    ]  
    

@register_snippet
class PortfolioCategory(models.Model):
    """ Portfolio category for a snippet """
    name = models.CharField("nom", max_length=50)

    panels = [
        FieldPanel("name"),
    ]

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "catégorie de projet"
        verbose_name_plural = "catégories de projets"

