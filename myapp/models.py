
from django.db import models

# Create your models here.


class LinkUrl(models.Model):
    link=models.CharField(max_length=1000)
    slug=models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.link