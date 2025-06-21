from django.conf import settings
from django.db import models


class Reviews(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey('catalogue_module.Books', on_delete=models.CASCADE)
    review = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.book.__str__()
