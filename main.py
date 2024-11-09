
import random
import string

while True:
    len_senha = int(input("Qual Tamanho da Senha? "))
    if len_senha >= 6:
        break
    else:
        print("O tamanho da senha deve ter no mínimo 6. Tente Novamente!")
            
add_letra_Maiuscula = input("Incluir Letra Maíscula? \n [1] Sim \n [2] Não: \n")
add_letra_Minuscula = input("Incluir Letra Minuscula? \n [1] Sim \n [2] Não: \n")
add_carater_especial = input("Incluir Caracter Especial? \n [1] Sim \n [2] Não: \n")

letras_maiusculas = string.ascii_uppercase
letras_minusculas = string.ascii_lowercase 
caracteres_especiais = string.punctuation

senha_gerada = []

if add_letra_Maiuscula == '1':
    senha_gerada.append(random.choice(letras_maiusculas))
    
if add_letra_Minuscula == '1':
    senha_gerada.append(random.choice(letras_minusculas))
    
if add_carater_especial == '1':
    senha_gerada.append(random.choice(caracteres_especiais))


while len(senha_gerada) < len_senha:
    senha_gerada.append(str(random.randint(0,9)))
    
random.shuffle(senha_gerada)
senha_gerada = ''.join(senha_gerada)  
print(senha_gerada)
  