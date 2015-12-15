from django.db import models

# Create your models here.
class Cat_color(models.Model):
    cat_color = models.CharField(max_length=200)

class Cat(models.Model):
    cat_name = models.CharField(max_length=200)
    cat_color = models.ForeignKey(Cat_color, on_delete=models.CASCADE)


