from django.db import models

class Product(models.Model):
    nameofprod = models.CharField(max_length=100) #Название продукта
    price = models.CharField(max_length=50) #Цена
    date = models.DateField() #Дата поступления в продажу
    country = models.CharField(max_length=100) #Страна-изготовитель

    def __str__(self):
        return self.nameofprod

