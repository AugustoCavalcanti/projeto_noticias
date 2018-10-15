from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    nome = models.CharField('Nome', max_length=128)
    data_de_nascimento = models.DateField('Data de nascimento', blank=True, null=True)
    telefone_celular = models.CharField('Telefone celular', max_length=15, help_text='Número de telefone celualr no formato (99) 99999-9999', null=True, blank=True)
    telefone_fixo = models.CharField('Telefone fixo1', max_length=14, help_text='Número de telefone fixo no formato (99) 9999-9999', null=True, blank=True)
    email = models.EmailField('E-mail', null=True, blank=True)

    def __str__(self):
        return self.nome

class Tag(models.Model):
    nome = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.SlugField(max_length=64)

    def __str__(self):
        return self.nome

class Noticia(models.Model):
    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
    titulo = models.CharField('Título', max_length=128)
    conteudo = models.TextField('Conteúdo')
    autor = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    data_de_publicacao = models.DateTimeField('Data de publicação', blank=True, null=True)

    def __str__(self):
        return self.titulo