from dataclasses import dataclass

@dataclass
class Produto:
    nome: str
    preco: float
    quanridade: int = 0

    def exibir_informacoes(self) -> str:
        return (
            f"Produto: {self.nome}, preço: {self.preco}, Quantidade: {self.quanridade}"
        )

produto1 = Produto("Caneta", 1.50, 100)
print(produto1.exibir_informacoes())
