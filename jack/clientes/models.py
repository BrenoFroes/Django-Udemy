from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30,null=True,blank=True)
    last_name=models.CharField(max_length=30,null=True,blank=True)
    age = models.IntegerField()
    salaray = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
