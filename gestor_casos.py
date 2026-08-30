class Nodo:
    """Nodo para lista simplemente enlazada que almacena un ciudadano/caso."""
    def __init__(self, datos):
        self.datos = datos
        self.siguiente = None


class Ciudadano:
    """Clase que representa a un ciudadano con su solicitud o denuncia."""
    def __init__(self, nombre, documento, tipo_caso, descripcion, prioridad):
        self.nombre = nombre
        self.documento = documento
        self.tipo_caso = tipo_caso
        self.descripcion = descripcion
        self.prioridad = prioridad


class GestorCasos:
    """Gestor de casos que usa una lista simplemente enlazada para organizar
    los casos según su nivel de prioridad (1 = más alto, 4 = más bajo)."""
    def __init__(self):
        self.cabeza = None

    def insertar(self, ciudadano):
        """Inserta un nuevo ciudadano/caso en la lista ordenado por prioridad.
        Los casos de prioridad 1 van al frente, seguidos de 2, 3 y 4."""
        nuevo_nodo = Nodo(ciudadano)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        elif self.cabeza.datos.prioridad >= ciudadano.prioridad:
            # Prioridad más alta (número más bajo) que la cabeza
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None and actual.siguiente.datos.prioridad < ciudadano.prioridad:
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        """Recorre la lista y muestra la información de cada ciudadano/caso."""
        actual = self.cabeza
        while actual is not None:
            d = actual.datos
            print(f"Nombre: {d.nombre}")
            print(f"Documento: {d.documento}")
            print(f"Tipo de caso: {d.tipo_caso}")
            print(f"Descripción: {d.descripcion}")
            print(f"Prioridad: {d.prioridad}")
            print("---")
            actual = actual.siguiente