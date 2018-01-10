#Escreva um programa que leia um valor em metros e o exiba convertido em centímetro e milímetros.
#km, hm, dam, m, dm, cm, mm

medida  = float(input('Uma distância em metros: '))

km = medida * 1000
hm = medida * 100
dam = medida * 10
m = medida * 1
cm = medida * 100
mm = medida * 1000

print('A medida de {}m corresponde a {:.0f}km, {:.0f}hm, {:.0f}dam, {:.0f}m, {:.0f}cm e {:.0f}mm'.format(medida, km, hm, dam, m, cm, mm))

