def divide (x, y):
    try:
        resultado = x / y
    
    except ZeroDivisionError:
        print("Opa, para aí! Você está tentando dividir por zero!!!")
    
    else:
        print("Certa ! A sua resposta: ", resultado)
    
    finally:
        # Este bloco sempre será executado!
        # Independente de ocorrer erro ou não
        print('Isso sempre aparecerá')

divide(3, 2)
divide(3, 0)
