from django.db import models

# Create your models here.


class Food(models.Model):

    foodId = models.AutoField(primary_key=True)
    foodTitle = models.CharField(max_length=20, default='Burger')
    foodName = models.CharField(max_length=50)
    foodType = models.CharField(max_length=10)
    foodPrice = models.FloatField()
    foodDesc = models.TextField()
    foodImage = models.ImageField(
        upload_to='foodimage/', default='NO-Image.jpg')

    def __str__(self):
        return f"{self.foodName}-{self.foodType}"
