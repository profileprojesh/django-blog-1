# Generated by Django 3.1.1 on 2021-03-03 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='default_blog_image.jpg', upload_to='blog_pics'),
        ),
    ]
