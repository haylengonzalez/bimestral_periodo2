print("--------------------------------")
print("-------NOTAS ESTUDIANTES--------")
print("--------------------------------")

#Entrada 
cod = int(input("Digite el codigo del estudiante"))
if cod!=0:
    nota1 = float(input("Digite la nota del parcial no. 1:"))
    nota2 = float(input("Digite la nota del parcial no. 2:"))
    nota3 = float(input("Digite la nota del parcial no. 3:"))
else:
    print("Fin de los datos de entrada")
#Procesamiento
reprobados = 0

while cod != 0:
    nota_final = (nota1 + nota2 + nota3)/3
    print ("El estudiante de codigo " + str(cod) + "obtuvo ua nota definitiva de " + str(nota_final))
    if nota final < 3:
        reprobados = reprobados +1
#Entrada
cod = int(input("Digite el codigo del estudiante: "))
if cod!=0:
    nota1 = float(input("Digite la nota del parcial no. 1:"))
    nota2 = float(input("Digite la nota del parcial no. 2:"))
    nota3 = float(input("Digite la nota del parcial no. 3:"))
    nota4 = float(input("Digite la nota del parcial no. 4:"))
    nota5 = float(input("Digite la nota del parcial no. 5:"))
else:
    print("Fin de los datos de entrada")
#Salida
print("Cantidad de estudiante que reprobaron la materia: " + str(reprobados))
print("Eso era...")