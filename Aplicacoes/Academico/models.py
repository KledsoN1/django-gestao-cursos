from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    
    nome = models.CharField(max_length=50) 
    
    creditos = models.PositiveSmallIntegerField()
    
    
    def __str__(self):
        return f"{self.nome} ({self.creditos} créditos)"
