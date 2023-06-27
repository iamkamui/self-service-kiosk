from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Category(models.Model):
    name = models.CharField(_("name"), max_length=50)
    created_at = models.DateTimeField(_("created"), auto_now_add=True)
    modified_at = models.DateTimeField(_("modified"), auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categorys'
    
    def __str__(self) -> str:
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(_('name'), max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(_("created"), auto_now_add=True)
    modified_at = models.DateTimeField(_("modified"), auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self) -> str:
        return f'{self.name}'