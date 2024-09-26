
from abc import ABC, abstractmethod

class Prestamo(ABC):
    @abstractmethod
    def prestar(self):
        pass

    @abstractmethod
    def devolver(self):
        pass

class Material(ABC):
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    @abstractmethod
    def mostrar_informacion(self):
        pass

class Libro(Material, Prestamo):
    def __init__(self, titulo, autor, año, num_paginas):
        super().__init__(titulo, autor, año)
        self.num_paginas = num_paginas
        self.prestado = False

    def mostrar_informacion(self):
        print(f"Libro: {self.titulo}, Autor: {self.autor}, Año: {self.año}, Páginas: {self.num_paginas}")

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print(f"{self.titulo} ha sido prestado.")
        else:
            print(f"{self.titulo} ya está prestado.")

    def devolver(self):
        if self.prestado:
            self.prestado = False
            print(f"{self.titulo} ha sido devuelto.")
        else:
            print(f"{self.titulo} no estaba prestado.")

class Revista(Material):
    def __init__(self, titulo, autor, año, numero_edicion):
        super().__init__(titulo, autor, año)
        self.numero_edicion = numero_edicion

    def mostrar_informacion(self):
        print(f"Revista: {self.titulo}, Autor: {self.autor}, Año: {self.año}, Edición: {self.numero_edicion}")

class DVD(Material, Prestamo):
    def __init__(self, titulo, autor, año, duracion):
        super().__init__(titulo, autor, año)
        self.duracion = duracion
        self.prestado = False

    def mostrar_informacion(self):
        print(f"DVD: {self.titulo}, Director: {self.autor}, Año: {self.año}, Duración: {self.duracion} mins")

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print(f"{self.titulo} ha sido prestado.")
        else:
            print(f"{self.titulo} ya está prestado.")

    def devolver(self):
        if self.prestado:
            self.prestado = False
            print(f"{self.titulo} ha sido devuelto.")
        else:
            print(f"{self.titulo} no estaba prestado.")

def obtener_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingresa un número válido.")

def listar_materiales_prestados(materiales):
    prestados = [material for material in materiales if isinstance(material, Prestamo) and material.prestado]
    if prestados:
        print("Materiales prestados:")
        for material in prestados:
            material.mostrar_informacion()
    else:
        print("No hay materiales prestados en este momento.")

def menu():
    materiales = []

    while True:
        print("\n--- Menú de Biblioteca ---")
        print("1. Agregar Libro")
        print("2. Agregar Revista")
        print("3. Agregar DVD")
        print("4. Mostrar todos los materiales")
        print("5. Prestar material")
        print("6. Devolver material")
        print("7. Listar materiales prestados")
        print("8. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            titulo = input("Ingresa el título del libro: ")
            autor = input("Ingresa el autor del libro: ")
            año = obtener_numero("Ingresa el año del libro: ")
            num_paginas = obtener_numero("Ingresa el número de páginas: ")
            libro = Libro(titulo, autor, año, num_paginas)
            materiales.append(libro)
            print(f"Libro '{titulo}' agregado.")

        elif opcion == '2':
            titulo = input("Ingresa el título de la revista: ")
            autor = input("Ingresa el autor de la revista: ")
            año = obtener_numero("Ingresa el año de la revista: ")
            numero_edicion = obtener_numero("Ingresa el número de edición de la revista: ")
            revista = Revista(titulo, autor, año, numero_edicion)
            materiales.append(revista)
            print(f"Revista '{titulo}' agregada.")

        elif opcion == '3':
            titulo = input("Ingresa el título del DVD: ")
            autor = input("Ingresa el director del DVD: ")
            año = obtener_numero("Ingresa el año del DVD: ")
            duracion = obtener_numero("Ingresa la duración del DVD en minutos: ")
            dvd = DVD(titulo, autor, año, duracion)
            materiales.append(dvd)
            print(f"DVD '{titulo}' agregado.")

        elif opcion == '4':
            if materiales:
                for material in materiales:
                    material.mostrar_informacion()
            else:
                print("No hay materiales en la lista.")

        elif opcion == '5':
            titulo = input("Ingresa el título del material a prestar: ")
            for material in materiales:
                if material.titulo == titulo:
                    if isinstance(material, Prestamo):
                        material.prestar()
                    else:
                        print("El material no se puede prestar.")
                    break
            else:
                print("Material no encontrado.")

        elif opcion == '6':
            titulo = input("Ingresa el título del material a devolver: ")
            for material in materiales:
                if material.titulo == titulo:
                    if isinstance(material, Prestamo):
                        material.devolver()
                    else:
                        print("El material no se puede devolver.")
                    break
            else:
                print("Material no encontrado.")

        elif opcion == '7':
            listar_materiales_prestados(materiales)

        elif opcion == '8':
            print("Saliendo...")
            break

        else:
            print("Opción no válida, por favor elige otra.")

if __name__ == "__main__":
    menu()
