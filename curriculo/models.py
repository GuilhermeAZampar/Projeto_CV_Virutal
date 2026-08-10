from django.db import models

# Create your models here.
class Projeto(models.Model):
    nome= models.CharField(max_length=100)
    descricao=models.TextField()
    tecnologia=models.CharField(max_length=100)
    github=models.URLField()

