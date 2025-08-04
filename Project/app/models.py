from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Time(models.Model):
    nome = models.CharField()
    descricao = models.CharField()
    criador = models.ForeignKey(User, on_delete=models.PROTECT, name='criador')
    membros = models.ManyToManyField(User, related_name='membros')



    class Meta:
        pass


class Tarefa(models.Model):
    titulo = models.CharField()
    descricao = models.CharField()
    status = models.CharField()
    responsavel = models.ForeignKey(User, on_delete=models.PROTECT, name='responsavel')
    time = models.ForeignKey(Time, on_delete=models.PROTECT, name='time')
    prazo = models.DateField(blank=False, null=False)

    class Meta:
        



