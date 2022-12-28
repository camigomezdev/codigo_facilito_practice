from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django_countries.fields import CountryField

class City(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='citiesapp/photos')
    population = models.IntegerField()
    country = CountryField()

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    text = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

