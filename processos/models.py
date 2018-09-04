from django.db import models


class Versao(models.Model):
    numero = models.CharField(max_length=3)

    def __str__(self):
        return self.numero

    class Meta:
        ordering = ['numero']
        verbose_name = 'Versão'
        verbose_name_plural = 'Versões'


class GrupoProcesso(models.Model):
    numero = models.ForeignKey(Versao, on_delete=models.CASCADE)
    sequencia = models.IntegerField(unique=True)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.descricao

    class Meta:
        ordering = ['sequencia']
        verbose_name = 'Grupo de Processo'
        verbose_name_plural = 'Grupos de Processos'


class AreaConhecimento(models.Model):
    numero = models.ForeignKey(Versao, on_delete=models.CASCADE)
    codigo = models.IntegerField(unique=True)
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['codigo']
        verbose_name = 'Área de Conhecimento'
        verbose_name_plural = 'Áreas de Conhecimento'


class Entrada(models.Model):
    sequencia = models.IntegerField(unique=True)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['sequencia']
    

class EntradaDetalhe(models.Model):
    nome = models.CharField(max_length=50)


class Saida(models.Model):
    sequencia = models.IntegerField(unique=True)
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['sequencia']


class Ferramenta(models.Model):
    sequencia = models.IntegerField(unique=True)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['sequencia']


class Processo(models.Model):
    grupo_processo = models.ForeignKey(GrupoProcesso, on_delete=models.CASCADE)
    area_conhecimento = models.ForeignKey(
        AreaConhecimento, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=50)
    descricao = models.CharField(max_length=300)
    
    def __str__(self):
        return self.codigo + ' ' + self.name

    class Meta:
        ordering = ['codigo']


class EntradaProcesso(models.Model):
    entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.entrada) + " ==> " + str(self.processo)

    class Meta:
        ordering = ['entrada']
        unique_together = ('entrada', 'processo')


class SaidaProcesso(models.Model):
    saida = models.ForeignKey(Saida, on_delete=models.CASCADE)
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.saida) + " ==> " + str(self.processo)

    class Meta:
        unique_together = ('saida', 'processo')


class FerramentaProcesso(models.Model):
    ferramenta = models.ForeignKey(Ferramenta, on_delete=models.CASCADE)
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.ferramenta) + " ==> " + str(self.processo)

    class Meta:
        unique_together = ('ferramenta', 'processo')
