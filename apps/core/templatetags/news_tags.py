from django import template

register = template.Library()

@register.inclusion_tag('partials/read_more.html')
def read_more(text, limit=100):
    return {
        'start': text[:limit],
        'end': text[limit:]
    }

@register.inclusion_tag('partials/category_badge.html')
def category_badge(name, color):
    return {
        'name': name,
        'color': color,
    }