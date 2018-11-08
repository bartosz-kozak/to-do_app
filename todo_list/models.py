from django.db import models

# Create your models here.

class List(models.Model):
    ithem = models.CharField(max_length=200) 
    complited = models.BooleanField(default=False)

    def __str__(self):
        return self.ithem
