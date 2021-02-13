import datetime

from django.db import models
from django.utils import timezone


class Member(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
# pour afficher dans le shell le string et non object ...
    def __str__(self):
        return 'Member : {} {}'.format(self.firstname, self.lastname)


# Create your models here.
