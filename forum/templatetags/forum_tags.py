from django import template
import forum.views as views

register = template.Library()


@register.simple_tag()
def get_category():
    return views.cats
