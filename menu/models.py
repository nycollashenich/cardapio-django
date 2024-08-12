from django.db import models

class Base(models.Model):
    created_at = models.DateField('Criado em', auto_now_add=True)
    modificated = models.DateField('Modificado', auto_now=True)
    active = models.BooleanField('Ativo?', default=True)

    class Meta():
        abstract = True

class Category(Base):
    CATEGORY_MENU_CHOICES = [
        ('bebida', 'Bebida'),
        ('hamburguer', 'Hamburguer'),
        ('pizza', 'Pizza'),
    ]
    category = models.CharField(max_length=35, choices=CATEGORY_MENU_CHOICES)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.category