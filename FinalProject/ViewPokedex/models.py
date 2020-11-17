from django.db import models

# Create your models here.

class Trainer(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)

    def __str__(self):
        return (self.first_name + ' ' + self.last_name)        
class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    type1 = models.CharField(max_length=20)
    type2 = models.CharField(max_length=20)
    hp = models.IntegerField()
    trainers = models.ManyToManyField(Trainer, blank=True)

    def __str__(self):
        return(self.name)

    @property
    def types(self):
        return (self.type1 + ' ' + self.type2)

