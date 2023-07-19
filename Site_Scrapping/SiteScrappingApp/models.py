from django.db import models

class Resultat(models.Model):
    designation = models.CharField(max_length=255)
    image1 = models.URLField()
    prix1 = models.DecimalField(max_digits=10, decimal_places=2)
    site1 = models.CharField(max_length=100)
    image2 = models.URLField()
    prix2 = models.DecimalField(max_digits=10, decimal_places=2)
    site2 = models.CharField(max_length=100)

    def __str__(self):
        return self.designation
