from django.db import models
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
)
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)
from .blocks import EducationBlock



class Skills(models.Model):
    title = models.CharField("titre", max_length=150, blank=True)

    panels = [
        FieldPanel("title"),
    ]

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Compétence et savoir-faire"
        verbose_name_plural="Compétences et savoir-faire"



class Tool(models.Model):
    title = models.CharField("titre", max_length=150, blank=True)
    icon = models.CharField("icône", max_length=150, blank=True, help_text="Renseigner le nom de l'icône. (Voir sur Devicon)")
    background_color = models.CharField(help_text="Format Hexadécimal #f20000", max_length=7, default="")
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Image background",
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("icon"),
        FieldPanel("background_color"),
        FieldPanel("image"),
    ]

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Outil de développement"
        verbose_name_plural="Outils de développement"


class Interest(models.Model):
    title = models.CharField("titre", max_length=150, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Image background",
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("image"),
    ]

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Centre d'intérêt"
        verbose_name_plural="Centres d'intérêts"



@register_setting(icon="globe")
class SocialSettings(BaseGenericSetting):
    codepen_url = models.URLField(verbose_name="Codepen URL", blank=True)
    discord_url = models.URLField(verbose_name="Discord URL", blank=True)
    facebook_url = models.URLField(verbose_name="Facebook URL", blank=True)
    github_url = models.URLField(verbose_name="GitHub URL", blank=True)
    instagram_url = models.URLField(verbose_name="Instagram URL", blank=True)
    linkedin_url = models.URLField(verbose_name="LinkedIn URL", blank=True)
    mastodon_url = models.URLField(verbose_name="Mastodon URL", blank=True)
    pinterest_url = models.URLField(verbose_name="Pinterest URL", blank=True)
    snapchat_url = models.URLField(verbose_name="Snapchat URL", blank=True)
    telegram_url = models.URLField(verbose_name="Telegram URL", blank=True)
    tiktok_url = models.URLField(verbose_name="TikTok URL", blank=True)
    twitch_url = models.URLField(verbose_name="Twitch URL", blank=True)
    whatsapp_url = models.URLField(verbose_name="WhatsApp URL", blank=True)
    x_url = models.URLField(verbose_name="X URL (ex twitter)", blank=True)
    youtube_url = models.URLField(verbose_name="Youtube URL", blank=True)

    class Meta:
        verbose_name = "Paramètres des réseaux sociaux"

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("codepen_url"),
                FieldPanel("discord_url"),
                FieldPanel("facebook_url"),
                FieldPanel("github_url"),
                FieldPanel("instagram_url"),
                FieldPanel("linkedin_url"),
                FieldPanel("mastodon_url"),
                FieldPanel("pinterest_url"),
                FieldPanel("snapchat_url"),
                FieldPanel("telegram_url"),
                FieldPanel("tiktok_url"),
                FieldPanel("twitch_url"),
                FieldPanel("whatsapp_url"),
                FieldPanel("x_url"),
                FieldPanel("youtube_url"),
            ],
            "Paramètres des réseaux sociaux",
        )
    ]



@register_setting(icon="cog")
class MyProfileSettings(BaseGenericSetting):
    birthday = models.DateField("date de naissance", blank=True, null=True, auto_now=False, auto_now_add=False)
    phone_number = models.CharField("numéro de téléphone", max_length=14, blank=True)
    contact_mail = models.EmailField("e-mail de contact", max_length=254, blank=True)
    city = models.CharField("ville", max_length=254, blank=True)
    SCHOOL_DEGREE=[
            ("", "Selectionnez un niveau"),
            ("cap", "CAP"),
            ("bep", "BEP"),
            ("bac", "BAC"),
            ("bac+2", "BAC+2"),
            ("bac+3", "BAC+3"),
            ("bac+4", "BAC+4"),
            ("bac+5", "BAC+5"),
            ("bac+8", "BAC+8"),
    ]
    highest_degree = models.CharField("diplôme le plus élevé", 
                                      max_length=5,
                                      choices=SCHOOL_DEGREE,
                                      default="cap")
    
    class Meta:
        verbose_name = "Paramètres de mon profil"

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("birthday"),
                FieldPanel("phone_number"),
                FieldPanel("contact_mail"),
                FieldPanel("city"),
                FieldPanel("highest_degree"),
            ],
            "Paramètres de mon profil",
        )
    ]


@register_setting(icon='image')
class ImageDefault(BaseGenericSetting):
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Image Default",
    )

    panels = [
        FieldPanel('image'),
    ]

