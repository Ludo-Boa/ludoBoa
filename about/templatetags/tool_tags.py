from django import template
from django.shortcuts import get_object_or_404
from base.models import Tool

register = template.Library()



# Tool snippets
@register.inclusion_tag('about/tags/tools.html', takes_context=True)
def tools(context):
    tools = Tool.objects.all()
    return {
        'tools': tools,
        'request': context['request'],
    }