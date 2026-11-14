
from pasajero import Pasajero


class MiCola:
    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def encolar(self, pasajero):
        if self.buscar(pasajero.numero) != -1:
            print("  El número de pasajero ya existe en la cola.")
            return False
        if self.cantidad == self.capacidad:
            print("  La cola está llena.")
            return False
        self.datos[self.cantidad] = pasajero
        self.cantidad += 1
        return True

    def listar(self):
        if self.esta_vacia():
            print("  (cola vacía)")
            return
        for i in range(self.cantidad):
            if i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FRENTE")
            elif i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← FINAL")
            else:
                print(f"  [{i}] {self.datos[i]}")

    def desencolar(self):
        if self.esta_vacia():
            return None
        pasajero = self.datos[0]
        for i in range(1, self.cantidad):
            self.datos[i - 1] = self.datos[i]
        self.datos[self.cantidad - 1] = None
        self.cantidad -= 1
        return pasajero

    def ver_frente(self):
        if self.esta_vacia():
            return None
        return self.datos[0]

    def buscar(self, numero):
        for i in range(self.cantidad):
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
        vueltas = self.cantidad
        eliminado = False

        for i in range(vueltas):
            pasajero = self.desencolar()
            if pasajero.numero == numero:
                eliminado = True
            else:
                self.encolar(pasajero)

        return eliminado

    def copiar(self):
        nueva_cola = MiCola(self.capacidad)
        for i in range(self.cantidad):
            nueva_cola.encolar(self.datos[i])
        return nueva_cola

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0
