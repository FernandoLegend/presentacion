#mensaje de entrada
print("Calculadora Basica")
print("Sumar opcion 1")
print("Restar opcion 2")
print("Multiplicar opcion 3")
print("Dividir opcion 4")
#eleccion de opcion
opc=(int)
opc=(input("Ingrese tipo de operacion:"))
#creacion de variables
n1=(float)
n2=(float)
resultado=(float)
suma=(float)
#Solicitud de datos
n1=(input("Ingrese primer valor:"))
n2=(input("Ingrese segundo valor:"))
#operaciones aritmeticas con bucles
while opc==1:
    opc=10
    resultado=n1+n2
while opc==2:
    opc=10
    resultado=n1-n2
while opc==3:
    opc=10
    resultado=n1*n2
while opc==4:
    opc=10
    resultado=n1/n2
print(resultado)
#Fernando marin C.I. 28.721.624
raw_input()