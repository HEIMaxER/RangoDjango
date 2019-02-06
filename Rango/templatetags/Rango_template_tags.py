from django import template
from Rango.models import Category

register = template.Library()

@register.inclusion_tag('Rango/cats.html')
def get_category_list(cat = None):
    return {'cats': Category.objects.all(), 'active_cat': cat}