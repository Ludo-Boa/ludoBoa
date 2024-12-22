from django import template
from base.models import Interest

register = template.Library()



# Interest snippets
@register.inclusion_tag('about/tags/interests.html', takes_context=True)
def interests(context):
    interests = Interest.objects.all()
    
    return {
        'interests': interests,
        'request': context['request'],
    }