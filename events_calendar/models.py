from django.db import models


class Calendar(models.Model):
    name = models.CharField(max_length=255)
    html_embed_code = models.TextField()

    def __str__(self):
        return str(self.name)
