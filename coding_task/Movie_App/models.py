from django.db import models

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    imgPath = models.CharField(max_length=200)
    duration = models.IntegerField()
    genre = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    type = models.CharField(max_length=20,  null=True)
    label = models.CharField(max_length=20,  null=True)
    userRating = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

