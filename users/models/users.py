from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField('Nombre', max_length=300, null=True, blank=True)
    phone = models.CharField('Telefono', max_length=15, null=True, blank=True)
    age = models.IntegerField('Edad',null=True, blank=True)
    created = models.DateTimeField('Creado',auto_now_add=True)

    def __str__(self):
        return self.name


