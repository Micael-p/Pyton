import re

texto = "Escrevendo um numero de telefone bacana (123) 456-7890"
padrao = r'\(\d{3}\) \d{3}-\d{4}'
# Padrão para encontrar números de telefone no formato (XXX) XXX-XXXX

resultado = re.search(padrao, texto)

if resultado:
    numero_telefone = resultado.group()
    print("Número de telefone encontado: ", numero_telefone)
else:
    print("Número de telefone não encontrado.")
