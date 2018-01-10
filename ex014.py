#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

c = float(input('Informe a temperatura em ªC: '))
f = ((9*c)/5) + 32
print('A temperatura de {0}ºC corresponde a {1}ºF!'.format(c, f))
