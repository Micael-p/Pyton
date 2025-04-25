from datetime import date
from pessoa import Pessoa
from marca import Marca
from veiculo import Veiculo

# Criando uma instancia de Pessoa
pessoa1 = Pessoa(cpf=1234567890, nome="Micael", nascimento=date(1984, 7, 26), oculos=True)

# Criando uma instancia de Marca
marca1 = Marca(id=1, nome="Fiat", sigla="FIA")

# Criando uma instancia de Veiculo
veiculo1 = Veiculo(placa="JWU7H93", cor="Vermelho", proprietario=pessoa1, marca=marca1)
