from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    image = models.ImageField(default = 'default_user_image.png', upload_to='user_profile_pics')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        img=Image.open(self.image.path)
        if img.width>300 or img.height >300:
            outputsize = (300,300)
            img.thumbnail(outputsize)
        img.save(self.image.path)
        return super().save()    
