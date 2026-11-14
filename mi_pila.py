
from pasajero import Pasajero


class MiPila:
    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def apilar(self, pasajero):
        if self.buscar(pasajero.numero) != -1:
            print("  El número de pasajero ya existe en la pila.")
            return False
        if self.cantidad == self.capacidad:
            print("  La pila está llena.")
            return False
        self.datos[self.cantidad] = pasajero
        self.cantidad += 1
        return True

    def listar(self):
        if self.esta_vacia():
            print("  (pila vacía)")
            return
        for i in range(self.cantidad - 1, -1, -1):
            if i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← TOPE")
            elif i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FONDO")
            else:
                print(f"  [{i}] {self.datos[i]}")

    def desapilar(self):
        if self.esta_vacia():
            return None
        pasajero = self.datos[self.cantidad - 1]
        self.datos[self.cantidad - 1] = None
        self.cantidad -= 1
        return pasajero

    def ver_tope(self):
        if self.esta_vacia():
            return None
        return self.datos[self.cantidad - 1]

    def buscar(self, numero):
        for i in range(self.cantidad - 1, -1, -1):
            if self.datos[i].numero == numero:
                return i
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        posicion = self.buscar(numero)
        if posicion == -1:
            return False
        self.datos[posicion].destino = nuevo_destino
        self.datos[posicion].asiento = nuevo_asiento
        return True

    def eliminar_por_numero(self, numero):
        auxiliar = MiPila(self.capacidad)
        eliminado = False

        while not self.esta_vacia() and self.ver_tope().numero != numero:
            auxiliar.apilar(self.desapilar())

        if not self.esta_vacia():
            self.desapilar()
            eliminado = True

        while not auxiliar.esta_vacia():
            self.apilar(auxiliar.desapilar())

        return eliminado

    def copiar(self):
        nueva_pila = MiPila(self.capacidad)
        for i in range(self.cantidad):
            nueva_pila.apilar(self.datos[i])
        return nueva_pila

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0
