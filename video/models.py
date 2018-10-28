from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    html_description = models.TextField()
    html_emded_code = models.TextField()
    image_thumbnail = models.ImageField()
    url = models.URLField()
    duration = models.DurationField()

    def __str__(self):
        return str(self.name)
