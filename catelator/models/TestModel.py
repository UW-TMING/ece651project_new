from django.db import models
from ckeditor.fields import RichTextField

class Article (models.Model):
    content = RichTextField("content")
    name    = models.CharField(default="123", max_length=50)