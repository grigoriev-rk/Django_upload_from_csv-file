from django.db import models
from datetime import datetime


class Phone(models.Model):

    id = models.IntegerField(primary_key=True, default=None)
    name = models.CharField(max_length=50, default=False)
    price = models.IntegerField(default=0)
    image = models.URLField(default=None)
    release = models.DateField(default=datetime.now().strftime("%Y-%m-%d"))
    lte_exists = models.BooleanField(default=0)
    slug = models.SlugField(max_length=100, unique=True)
