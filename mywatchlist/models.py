from django.db import models

# Create your models here.


class MyWatchList(models.Model):
    watched = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    rating_choices = [(str(i), str(i)) for i in range(1, 6)]
    rating = models.CharField(max_length=1,
                              choices=rating_choices, default='1')
    release_date = models.DateField()
    review = models.TextField()
