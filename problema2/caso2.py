"""Programa para calcualar la cantidad de números pares 
e impares que se digite"""

print("--------------------------------------")
print("--------NUMEROS PARES E IMPARES-------")
print("--------------------------------------")

#Entrada
numero = int(input("Digite un número entero positivo: "))

#Procesamiento
par = 0
impar = 0
while numero != 0:
    resultado = numero%2
    print(numero)
    if resultado == 0:
        par = par + 1
        numero = int(input("Digite un número entero positivo: "))
    else:
        impar = impar + 1
        numero = int(input("Digite un número entero positivo: "))

#Salida
print(str(par) + " números pares se digitaron")
print(str(impar) + " números impares se digitaron")
print("Thats all...")