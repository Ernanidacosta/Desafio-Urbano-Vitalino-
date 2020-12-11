from django.db import models
from cadas
# Create your models here.
class Planilha(models.Model):
    pasta = CharField()
    comarca = CharField()
    uf = CharField()
