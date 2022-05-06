from django.db import models
from django.utils import timezone


"""
CONTATOS

nome: STR * (obrigatório)
sobrenome: STR (opcional)
telefone: STR * (obrigatório)
email: STR (opcional)
data_criacao: DATETIME (automático)
descricao: texto
categoria: CATEGORIA (outro model)

CATEGORIA

nome: STR * (obrigatório)

-------------------------------------
comando de terminal para criar as migrações:
python manage.py makemigrations

e depois para inserir na base de dados:
python manage.py migrate

"""

class Categoria(models.Model):
    nome=models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=255) #definindo o atributo nome e definindo tamanho da string
    sobrenome = models.CharField(max_length=255, blank=True) # blank=True para deixar o atributo opcional
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao=models.DateTimeField(default=timezone.now()) #definindo atributo datetime
    descricao = models.CharField(max_length=255,blank=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.DO_NOTHING)
    mostrar =models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%M') #campo para adicionar fotos

    def __str__(self):
        return self.nome






