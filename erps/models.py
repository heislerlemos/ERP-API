from django.db import models



SEXO = (('masculino', 'M'), ('feminino', 'F'))
PROVINCIAS = (('Luanda', 'L'), ('Benguela', 'B'), ('Lubango', 'LB'), ('Soyo', 'S'), ('Cabinda', 'C'))
ESTADO = (('Casado', 'C'), ('Solteiro', 'S'), ('Divorciado', 'D'))


class Rh(models.Model):
    nome = models.CharField(max_length=50)
    genero = models.CharField(max_length=10 , choices=SEXO)
    provincias = models.CharField(max_length=20, choices=PROVINCIAS)
    email = models.CharField(max_length=50)
    nif =  models.IntegerField()
    data =  models.DateField()
    nacionalidade = models.CharField(max_length=50)
    telefone = models.IntegerField()

class Warehouse(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    serialnumber = models.IntegerField()
    data = models.DateField()


class Contabilidade(models.Model):
    descicao = models.CharField(max_length=100)
    data = models.DateField()
    gastos = models.IntegerField()
    credito = models.IntegerField()
