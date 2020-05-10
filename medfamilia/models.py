from django.db import models

# Create your models here.

class Especialidade (models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    descricao = models.TextField(verbose_name='Descrição')
    imagem = models.ImageField(upload_to='especialidades')

    def __str__ (self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name_plural = '02 - Especialidades'


class Consulta (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=100)
    especialidade = models.ForeignKey('Especialidade', on_delete=models.PROTECT)
    data = models.CharField(max_length=10)

    turnos = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde')
    ]

    turno = models.CharField(max_length=10, choices=turnos, default='manha')
    info_adicionais = models.TextField(blank=True)
    respondida = models.BooleanField()

    def __str__ (self):
        valor = "[Respondida] " if self.respondida else "[Em espera] "
        return valor + self.email

    class Meta:
        ordering = ['respondida', 'id']
        verbose_name_plural = '03 - Consultas'


class QuemSomos (models.Model):
    visao = models.TextField(verbose_name='Visão', max_length=300)
    missao = models.TextField(verbose_name='Missão', max_length=300)
    valores = models.TextField(verbose_name='Valores', max_length=300)

    class Meta:
        verbose_name = 'Quem Somos'
        verbose_name_plural = '01 - Quem Somos'