from django.db import models


class city(models.Model):
    Name=models.CharField(max_length=25,default='')

    def __str__(self):
        return self.Name