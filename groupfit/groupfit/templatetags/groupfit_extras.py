from django import template
register = template.Library

@register.filter
def get_value( dictionary, key ):
    value = dictionary.get( key )
    return value
