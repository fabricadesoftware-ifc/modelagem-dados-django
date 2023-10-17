from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=40)

    def __str__(self):
        return self.descricao
    
class Pais(models.Model):
    nome = models.CharField(max_length=60)

    def __str__(self):
        return self.nome

class TipoAtuacao(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Produtora(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
    
class Membro(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
    
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    ano = models.IntegerField()
    classificacao = models.IntegerField()
    duracao = models.TimeField()
    sinopse = models.TextField()
    produtora = models.ForeignKey(Produtora, on_delete=models.PROTECT)
    categorias = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.titulo
    
class Atuacao(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.PROTECT)
    membro = models.ForeignKey(Membro, on_delete=models.PROTECT)
    tipo_atuacao = models.ForeignKey(TipoAtuacao, on_delete=models.PROTECT)
    personagem = models.CharField(max_length=100, blank=True, null=True)