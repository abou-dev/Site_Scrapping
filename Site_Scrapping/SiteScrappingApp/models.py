from django.db import models

class Resultat(models.Model):
    designation = models.CharField(max_length=255)
    image = models.URLField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    site = models.CharField(max_length=100)

    def __str__(self):
        return self.designation
