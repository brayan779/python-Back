# pessoas/models.py

from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome

# Arquivo: teste.py

class Vendas:
    def __init__(self, produto, valor, data, forma_pagamento):
        self.produto = produto
        self.valor = valor
        self.data = data
        self.forma_pagamento = forma_pagamento

class Comanda:
    def __init__(self, codigo, data, produtos, total):
        self.codigo = codigo
        self.data = data
        self.produtos = produtos  # lista de produtos
        self.total = total

class ContasReceber:
    def __init__(self, convenio, data, valor, identificacao, particulares, marmitas):
        self.convenio = convenio
        self.data = data
        self.valor = valor
        self.identificacao = identificacao
        self.particulares = particulares
        self.marmitas = marmitas

class Suprimentos:
    def __init__(self, embalagens, bebidas, comidas, temperos, produtos_limpeza):
        self.embalagens = embalagens
        self.bebidas = bebidas
        self.comidas = comidas
        self.temperos = temperos
        self.produtos_limpeza = produtos_limpeza

class Caixa:
    def __init__(self, contas_receber, contas_pagar, forma_pagamento):
        self.contas_receber = contas_receber  # pode ser lista de ContasReceber
        self.contas_pagar = contas_pagar
        self.forma_pagamento = forma_pagamento