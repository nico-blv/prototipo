from django.db import models

# Create your models here.

class Vaca(models.Model):
    id = models.BigAutoField(primary_key=True)
    peso = models.TextField(verbose_name="Peso")
    raza = models.TextField(verbose_name="Raza", default="Vaca")
    sexo = models.TextField(verbose_name="Sexo")
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

    class Meta:
        ordering=["-created"]
