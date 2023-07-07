from django import template

register = template.Library()

@register.filter(name='has_group')
def has_group(user, groups):
    groups = groups.split()
    return user.groups.filter(name__in=groups).exists()