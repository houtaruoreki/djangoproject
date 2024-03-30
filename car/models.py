from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"
