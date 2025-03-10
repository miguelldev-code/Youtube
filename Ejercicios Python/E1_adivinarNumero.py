# Adivinar numero aleatorio del 1 al 10 y en caso de no acertar, 
# decir si es numero ingresado es mas alto o bajo.

# importar libreria random
import random

numeroAleatorio = random.randint(1, 10)
intento = int(input("Adivina el numero del 1 al 10"))

# while - comparacion y validacion

# numeroAleatorio = 5
# intento = 5

while intento != numeroAleatorio:
    if intento < numeroAleatorio:
        print("Numero mas alto")
    if intento > numeroAleatorio:
        print("Numero mas bajo")

    intento = int(input("Intenta de nuevo: "))

print("Acertaste!!")
