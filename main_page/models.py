from django.db import models


class Scene(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    file_video = models.FileField(blank=True, null=True)
    file_audio = models.FileField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    html_content = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class SocialMedia(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return str(self.name)
