from django.db import models


class Jogos(models.Model):
    times = models.CharField(max_length=50)
    placar = models.CharField(max_length=10)
    situacao = models.CharField(max_length=70)
    release_date = models.CharField(max_length=10)


class Jogadores(models.Model):
    OPTIONS = {
        ("F", "FEW"),
        ("S", "SOMETIMES"),
        ("Q", "QUITE"),
    }
    POSICAO = {
        ("G", "GOLEIRO"),
        ("Z", "ZAGUEIRO"),
        ("M", "MEIO CAMPO"),
        ("A", "ATACANTE"),
    }
    jogadores = models.CharField(max_length=50)
    frequencia = models.CharField(max_length=1, choices=OPTIONS)
    posicao = models.CharField(max_length=1, choices=POSICAO)
    gols = models.IntegerField()
