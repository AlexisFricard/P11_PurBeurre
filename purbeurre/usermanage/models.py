from django.db import models
from usermanage.storage_backends import PublicMediaStorage


# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(storage=PublicMediaStorage())

    class Meta:
        db_table = "image"
