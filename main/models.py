from django.db import models


class IndexBanners(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    is_active = models.BooleanField(default=True)
