"""
📌 Cálculo de áreas de figuras geométricas en Python  
Este programa permite calcular el área de:  
✅ Rectángulo  
✅ Triángulo  
✅ Círculo  
✅ Cuadrado  

🔹 Se solicita al usuario seleccionar una figura e ingresar los valores necesarios.  
🔹 Se utiliza `match-case` (switch) para gestionar las opciones.  
🔹 Cada cálculo está encapsulado en una función para mejor organización.  
"""
import math

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_area_cuadradro(lado):
    return lado ** 2

def calcular_area():
    print("Seleccione la figura para calcular el area: ")
    print("1. rectangulo")
    print("2. Triangulo")
    print("3. Circulo")
    print("4. Cuadrado")

    opcion = input("Ingrese el numero de la figura: ")

    match opcion:
        case "1":
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            area = calcular_area_rectangulo(base, altura)
            print(f"Area del rectangulo: {area}")
        case "2":
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            area = calcular_area_triangulo(base, altura)
            print(f"Area del triangulo: {area}")
        case "3":
            radio = float(input("Digite el radio: "))
            area = calcular_area_circulo(radio)
            print(f"Area del circulo: {area:.2f}")
        case "4":
            lado = float(input("Digite el lado: "))
            area = calcular_area_cuadradro(lado)
            print(f"Area del cuadrado: {area}")

        case _:
            print("X opcion no valida, Debe ser un numero del 1 al 4")

calcular_area()