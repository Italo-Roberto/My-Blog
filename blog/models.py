from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.CharField(max_length=200, null=True)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = 'blog'

    def __str__(self):
        return self.titulo