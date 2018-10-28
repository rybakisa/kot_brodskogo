from django.db import models


class ReadingMaterial(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    html_text = models.TextField()
    image_thumbnail = models.ImageField()
    image_head = models.ImageField()

    def __str__(self):
        return str(self.name)
