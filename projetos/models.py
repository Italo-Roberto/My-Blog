from django.db import models

# Create your models here.
class Projeto(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.CharField(max_length=200)
    tecnologias = models.TextField(max_length=200)
    detalhes = models.CharField(max_length=200)
    link = models.URLField(blank=False)
    foto = models.ImageField(upload_to='projetos/imagens/')

    def separaTecnologias(self):
        return self.tecnologias.split(' ')

    class Meta():
        db_table = 'projetos'

    def __str__(self):
        return self.titulo