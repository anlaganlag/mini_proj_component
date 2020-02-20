from django.db import models

class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    age = models.IntegerField(default=100)

    class Meta:
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name

