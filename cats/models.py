from django.db import models
from django.utils import timezone

# Create your models here.
class Toy(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Achievement(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Owner(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Cat(models.Model):
    class Meta:
        db_table = 'cats'
    name = models.CharField(max_length=15)
    color = models.CharField(max_length=20)
    birth_year = models.IntegerField(null=True)
    created = models.DateTimeField('created', auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, default=None)
    is_purebred = models.BooleanField(default=False)
    owner = models.ForeignKey(Owner, related_name='cats', on_delete=models.CASCADE)
    achievements = models.ManyToManyField(Achievement, through='AchievementCat')
    toys = models.ManyToManyField(Toy, through='FavouriteToyCat')

    def __str__(self):
        return f'{self.name}, {self.color}, {self.toys}'
    
    def delete (self): 
        self.deleted = timezone.now() 
        self.save()

# В этой модели будут связаны id котика и id его достижения
class AchievementCat(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.achievement} {self.cat}'
    

class FavouriteToyCat(models.Model):
    toy = models.ForeignKey(Toy, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.toy} {self.cat}'
