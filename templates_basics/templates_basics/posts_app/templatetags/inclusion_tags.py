from django import template
from datetime import datetime

register = template.Library()

@register.inclusion_tag('user-info.html', takes_context=True)
def user_info(context):
    if context.request.user.is_authenticated:
        return {
            'username': context.request.user.username
        }
    return {
        'username': 'Anonymous'
    }