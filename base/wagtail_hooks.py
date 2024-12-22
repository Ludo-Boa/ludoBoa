# myapp/wagtail_hooks.py
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from base.models import Skills, Tool, Interest


class SkillViewSet(SnippetViewSet):
    model = Skills

    panels = [
        FieldPanel("title"),
    ]

register_snippet(SkillViewSet)


class ToolViewSet(SnippetViewSet):
    model = Tool

    panels = [
        FieldPanel("title"),
        FieldPanel("icon"),
        FieldPanel("background_color"),
        FieldPanel("image"),
    ]

register_snippet(ToolViewSet)


class InterestViewSet(SnippetViewSet):
    model = Interest

    panels = [
        FieldPanel("title"),
        FieldPanel("image"),
    ]

register_snippet(InterestViewSet)