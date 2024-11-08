from django.db import models

class Servicio(models.Model):
    url = models.URLField(max_length=200)
    tag = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.tag