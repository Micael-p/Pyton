class Carro:
    def __init__(self, marca: str, modelo: str, ano: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

meu_carro = Carro("Toyota", "corolla", 2020)


print(meu_carro.marca, meu_carro.modelo, meu_carro.ano)
