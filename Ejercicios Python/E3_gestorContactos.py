"""
📌 Gestor de Contactos en Python  
Este programa permite agregar, buscar, eliminar y mostrar contactos  
usando un diccionario en Python. 
 
Conceptos Técnicos Aprendidos
🔹 Uso de diccionarios para almacenar contactos.
🔹 Funciones para organizar el código.
🔹 Bucle while con un menú interactivo.
🔹 Entrada y salida de datos con input() y print().
"""

#Diccionario para almacenar los contactos
contactos = {}

def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese numero de telefono: ")
    correo = input("Ingrese el correo: ")

    contactos[nombre] = {"Telefono":telefono, "Correo":correo}
    print(f"Contacto {nombre} agregado correctamente.\n")

def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto a buscar" )
    if nombre in contactos:
        print(f" Contacto encontrado: Telefono: {contactos[nombre]['Telefono']}  Correo: {contactos[nombre]['Correo']}\n")
    else:
        print("Contacto no encontrado")

def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto {nombre} se ha eliminado\n")
    else:
        print("Contacto no encontrado\n")

def mostrar_contacto():
    if not contactos:
        print("No hay contactos guardados\n")
    else:
        print("Lista contactos: ")
        for nombre, datos in contactos.items():
            print(f"{nombre}, {datos['Telefono']} y {datos['Correo']}\n")
        print()

def menu():
    while True:
        print("-------------------")
        print("Gestor de Contactos")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar contactos")
        print("5. Salir")
        print("-------------------")


        opcion = input("Elige una opcion (1-5)")

        match opcion:
            case "1":
                agregar_contacto()
            case "2":
                buscar_contacto()
            case "3":
                eliminar_contacto()
            case "4":
                mostrar_contacto()
            case "5":
                print("Saliendo del programa...")
                break
            case _:
                print("Opcion no valida, intente de nuevo")

menu()


