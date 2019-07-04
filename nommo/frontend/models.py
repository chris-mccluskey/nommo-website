from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    province = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

class Category(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Investment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rank = models.PositiveSmallIntegerField(blank=True, null=True)
    site = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Investment'
        verbose_name_plural = 'Investments'

# Create your models here.
