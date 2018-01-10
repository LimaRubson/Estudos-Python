
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo a todos as informações possíveis sobre ele.

a = input('Digite algo: ')#Retorna uma STRING independente do tipo
print('O tipo primitivo desse valor é ', type(a))
print("Só tem espaço? ", a.isspace())#Só tem espacos
print("É um número? ", a.isnumeric())#Verifica se tem um número
print("É alfabético? ", a.isalpha())#Verifica se é alfabético
print("É alfanumérico? ", a.isalnum())#Verifica se é alfanumérico
print("Está em maiúscula? ", a.isupper())#Verifica se está em maiúscula
print("Está em minúscula? ", a.islower())#Verifica se está em minúscula
print("Está capitalizada? ", a.istitle())#Verifica se está capitalizada
