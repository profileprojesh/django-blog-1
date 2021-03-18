import string
import random
from django.utils.text import slugify

def create_slug(title):
    slug_prefix = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
    return slug_prefix + '-' + slugify(title)
