from django.db import models
from django.core.urlresolvers import reverse


class Family(models.Model):
    family_name = models.CharField(max_length=250)
    family_location = models.CharField(max_length=250)
    family_logo = models.FileField()

    def __str__(self):
        return self.family_name

    def get_absolute_url(self):
        return reverse('tree:detail', kwargs={'pk': self.pk})


class Person(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    second_name = models.CharField(max_length=250)
    person_photo = models.FileField()
    date_of_birth = models.CharField(max_length=100)
    date_of_death = models.CharField(max_length=100)
    is_married = models.BooleanField(default=False)
    lives_in = models.CharField(max_length=100)
    person_descr = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name + ' ' + self.second_name

    def get_absolute_url(self):
        return reverse('tree:person_detail', kwargs={'pk': self.pk})
