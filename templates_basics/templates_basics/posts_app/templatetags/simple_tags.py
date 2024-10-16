from django import template
from datetime import datetime

register = template.Library()

@register.simple_tag(name="current_time")
def current_time(format_string="%T-%m-%d %H:%M:%S"):
    return datetime.now().strftime(format_string)