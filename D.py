from dataclasses import dataclass

@dataclass
class Produto:
    nome: str
    preco: float
    quanridade: int = 0

produto1 = Produto("Caneta", 1.50, 100)
print(produto1.nome, produto1.preco, produto1.quanridade)
