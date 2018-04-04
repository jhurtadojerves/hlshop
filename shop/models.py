from django.db import models


class Shop(models.Model):
    name = models.TextField()
    url = models.URLField(unique=True)
    vault = models.IntegerField(default=0)
    stars = models.IntegerField(default=0)
    opened = models.BooleanField(default=True)
    checked = models.BooleanField(default=False)
    error = models.BooleanField(default=False)
    last_month = models.BooleanField(default=False)

    def __str__(self):
        return self.name
