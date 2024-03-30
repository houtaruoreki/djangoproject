from django.db import models


class Animal(models.Model):
    species = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.color} {self.species} named {self.name}"
