from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .utils import create_slug
from PIL import Image




STATUS = (
    (0, 'Draft'),
    (1,'Published')
)

class Blog(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(default = 'default_blog_image.jpg', upload_to='blog_pics')
    status = models.IntegerField(choices=STATUS, default=1)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('each-post', kwargs={'slug':self.slug})

    def validate_author_with_user(self, user):
        if self.author.username == user.username:
            return True
                

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height >300 or img.width >300:
            output = (300, 300)
            img.thumbnail(output)
        img.save(self.image.path)    
        self.slug = create_slug(self.title)
        super(Blog, self).save()     



