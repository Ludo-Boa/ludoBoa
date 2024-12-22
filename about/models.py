from datetime import date
from django.utils import timezone
from urllib import request
from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from base.models import MyProfileSettings



class AboutPage(Page):
    title_intro = models.CharField("titre de l'intro", max_length=50, blank=True)
    intro = RichTextField(blank=True)
    image_profil = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Image Profil",
    )
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Image Banner",
    )

    content_panels = Page.content_panels + [
        FieldPanel('title_intro'),
        FieldPanel('intro'),
        FieldPanel('image_profil'),
        FieldPanel('hero_image'),
    ]

    def get_context(self, request):
        context = super(AboutPage, self).get_context(request)
        profile_settings = MyProfileSettings.load(request_or_site=request)

        # Calcul de l'age
        current_date = date.today()
        current_year = timezone.now().year
        birthday = profile_settings.birthday
        age = current_year - birthday.year - ((current_date.month, current_date.day) < (birthday.month, birthday.day))

        phone = profile_settings.phone_number
        city = profile_settings.city
        degree = profile_settings.highest_degree
        email = profile_settings.contact_mail

        # Compte le nombre de jours depuis le 6/02/2016
        # Qui correspond à 1 tasse de café par jour
        date_start = date(2016,2,6)
        delta = current_date - date_start
        coffe_cups = str(delta.days)

        # Calcule : nombre de ligne de code (moyenne) par projets 
        codeline_average = 5400
        #codeline = codeline_average * nb_projects

        # Années d'expérience
        exp = str(delta.days / 365 -1)

        context['age'] = age
        context['phone'] = phone
        context['city'] = city
        context['degree'] = degree
        context['email'] = email
        context['coffe_cups'] = coffe_cups
        context['exp'] = exp
        return context
    
