from gestor_casos import GestorCasos, Ciudadano


class Main:
    def __init__(self):
        self.gestor = GestorCasos()

    def ingresar_datos(self):
        nombre = input("Nombre: ")
        documento = input("Documento: ")
        tipo_caso = input("Tipo de caso: ")
        descripcion = input("Descripción: ")
        prioridad = int(input("Prioridad (1-4, 1=alta): "))
        ciudadano = Ciudadano(nombre, documento, tipo_caso, descripcion, prioridad)
        self.gestor.insertar(ciudadano)
        print("Ciudadano añadido correctamente.\n")

    def ejecutar(self):
        while True:
            print("1. Añadir ciudadano")
            print("2. Mostrar todos los casos")
            print("3. Salir")
            opcion = input("Opción: ")
            if opcion == "1":
                self.ingresar_datos()
            elif opcion == "2":
                self.gestor.mostrar()
            elif opcion == "3":
                break
            else:
                print("Opción no válida.\n")


if __name__ == "__main__":
    app = Main()
    app.ejecutar()