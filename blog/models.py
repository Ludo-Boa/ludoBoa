from django import forms
from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models.aggregates import Count

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.admin.panels import TabbedInterface, TitleFieldPanel, ObjectList
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from base.blocks import BaseStreamBlock


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Hero image",
    )

    def get_context(self, request):
        # Mettre à jour le contexte pour inclure uniquement les publications publiées, classées par chronologie inversée
        context = super().get_context(request)
        all_posts = self.get_children().live().public().order_by('-first_published_at')

        paginator = Paginator(all_posts, 9) # @todo change to 5 per page
        page = request.GET.get("page")
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)


        context['posts'] = posts
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]
    banner_panels = [
        FieldPanel('hero_image'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Contenu'),
        ObjectList(banner_panels, heading='Bannière'),
        ObjectList(Page.promote_panels, heading='Promotion'),
    ])




class BlogTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        
        return context




class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )




class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Bloc de contenu",
        blank=True,
        use_json_field=True,
    )
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Blogpage image",
    )
    authors = ParentalManyToManyField('blog.Author', blank=True)

    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
            FieldPanel('tags'),
        ], heading="Blog information"),
        FieldPanel('intro'),
        FieldPanel('hero_image'),
        FieldPanel('body'),
    ]

    def __str__(self):
        return self.title




@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=255)
    author_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('author_image'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Authors'