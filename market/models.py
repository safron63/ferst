from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    # Перевод на русский
    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255,verbose_name='Имя')
    isactive = models.BooleanField(verbose_name='Наличие')
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='Категория')

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.name
