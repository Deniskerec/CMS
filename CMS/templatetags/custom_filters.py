from django import template

register = template.Library()

@register.filter
def sum_amounts(queryset, field_name):
    return sum(getattr(item, field_name) for item in queryset)
