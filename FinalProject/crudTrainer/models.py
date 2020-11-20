from django.db import models       
class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    type1 = models.CharField(max_length=20)
    type2 = models.CharField(max_length=20)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    sp_atk = models.IntegerField()
    sp_def = models.IntegerField()
    speed = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return(self.name)

    @property
    def types(self):
        return (self.type1 + ' ' + self.type2)

class Trainer(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    home_town = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 10)
    fav_type = models.CharField(max_length = 20)
    discovered_pokemon = models.ManyToManyField(Pokemon, blank=True)

    def __str__(self):
        return (self.first_name + ' ' + self.last_name)        