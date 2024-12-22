from django import template
from base.models import Skills

register = template.Library()



# Skills snippets
@register.inclusion_tag('about/tags/skills.html', takes_context=True)
def skills(context):
    return {
        'skills': Skills.objects.all(),
        'request': context['request'],
    }