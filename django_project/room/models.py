from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Room, self).save(*args, **kwargs)

    def __str__(self):
        return self.name