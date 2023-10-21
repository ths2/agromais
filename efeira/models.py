from django.db import models
from django.contrib.auth.models import User

class Produtor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=200)
    contato = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/')
    data_inicio_colheita = models.DateField()
    data_fim_colheita = models.DateField()
    pronto_para_colheita = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    pontuacao = models.PositiveIntegerField()
    comentario = models.TextField()
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avaliação de {self.produto.nome} por {self.cliente.username}"

class Pedido(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, through='ItemPedido')
    data_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido de {self.cliente.username}"

class ItemPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"Item de {self.produto.nome} no Pedido de {self.pedido.cliente.username}"
