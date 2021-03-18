from django import template

register = template.Library()

@register.filter
def validate_author_with_user(user, author):
    if user == author:
        return True
    else:
        return False    
