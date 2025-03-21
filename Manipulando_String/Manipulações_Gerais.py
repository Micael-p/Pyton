texto = "Algum texto muito bacana pra ser escrito."

print (texto[0:20:2])

print (len(texto))

print (texto.count("a"))

print (texto.count("r", 5, 40))

print (texto.find("escrito"))

print ('texto' in texto)

novo_texto = texto.replace("bacana", "bolado")
print(novo_texto)

print(texto.startswith("algum"))
print(texto.startswith("texto"))

print(texto.endswith("escrito"))
print(texto.endswith("."))

print(texto.lower())
print(texto.upper())
print(texto.capitalize())
print(texto.title())
print(texto.swapcase())

print(' '.join(texto))
print(texto.split())
print(' '.join(texto.split()))
