from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=120)
    alias = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Heroes"