import re

def validar_email(email):
    padrao = r'\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    if re.match(padrao, email):
        return True
    else:
        return False

exemplo_emails = ["usuario@gmail.com", "outro@email.co.uk", "invalido@.com", "sem_arroba.com"]

for email in exemplo_emails:
    if validar_email(email):
        print(f"{email} é um endereço de e-mail valido.")
    else:
        print(f"{email} é um endereço de e-mail invalido.")
