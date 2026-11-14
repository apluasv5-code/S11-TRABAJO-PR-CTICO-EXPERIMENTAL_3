
from datetime import datetime
from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola


pila = MiPila(10)
cola = MiCola(10)


# -------------------- FUNCIONES DE APOYO --------------------

def leer_entero(mensaje, minimo=None):
    while True:
        try:
            numero = int(input(mensaje))
            if minimo is not None and numero < minimo:
                print(f"  Ingresa un número mayor o igual a {minimo}.")
            else:
                return numero
        except ValueError:
            print("  Debe ser un número entero.")


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("  Este campo no puede estar vacío.")


def leer_fecha():
    while True:
        fecha = leer_texto("  Fecha de vuelo (AAAA-MM-DD): ")
        try:
            fecha_valida = datetime.strptime(fecha, "%Y-%m-%d")
            if fecha_valida.strftime("%Y-%m-%d") == fecha:
                return fecha
        except ValueError:
            pass
        print("  Fecha inválida. Usa el formato AAAA-MM-DD.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ", 1)
    nombre = leer_texto("  Nombre: ")
    cedula = leer_texto("  Cédula: ")
    edad = leer_entero("  Edad: ", 0)
    fecha = leer_fecha()
    destino = leer_texto("  Destino: ")
    asiento = leer_texto("  Asiento: ").upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def datos_prueba():
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana", "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis", "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto", "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]


def mostrar_opciones(titulo, entrar, salir, ver):
    print(f"\n========== {titulo} ==========")
    print(f" 1. {entrar:<12}  2. Listar          3. {salir}")
    print(f" 4. {ver:<12}  5. Buscar          6. Modificar")
    print(" 7. Eliminar por número         8. Copiar")
    print(" 9. Longitud / ¿vacía?")
    print(" C. Cargar datos de prueba      0. Volver")


# -------------------- MENÚ 1: PILA --------------------

def menu_pila():
    while True:
        mostrar_opciones("MENÚ 1 · PILA (LIFO)", "Apilar", "Desapilar", "Ver tope")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if pila.apilar(pasajero):
                print("  Pasajero apilado correctamente.")

        elif op == "2":
            pila.listar()

        elif op == "3":
            pasajero = pila.desapilar()
            if pasajero is None:
                print("  La pila está vacía.")
            else:
                print(f"  Salió: {pasajero}")

        elif op == "4":
            pasajero = pila.ver_tope()
            if pasajero is None:
                print("  La pila está vacía.")
            else:
                print(f"  Tope: {pasajero}")

        elif op == "5":
            numero = leer_entero("  Número a buscar: ")
            posicion = pila.buscar(numero)
            if posicion == -1:
                print("  No existe ese pasajero.")
            else:
                print(f"  Encontrado en [{posicion}]: {pila.datos[posicion]}")

        elif op == "6":
            numero = leer_entero("  Número a modificar: ")
            destino = leer_texto("  Nuevo destino: ")
            asiento = leer_texto("  Nuevo asiento: ").upper()
            if pila.modificar(numero, destino, asiento):
                print("  Pasajero modificado correctamente.")
            else:
                print("  No existe ese pasajero.")

        elif op == "7":
            numero = leer_entero("  Número a eliminar: ")
            if pila.eliminar_por_numero(numero):
                print("  Pasajero eliminado correctamente.")
            else:
                print("  No existe ese pasajero.")

        elif op == "8":
            copia = pila.copiar()
            print("  Copia de la pila:")
            copia.listar()

        elif op == "9":
            print(f"  Longitud: {pila.longitud()}")
            print(f"  ¿Está vacía?: {'Sí' if pila.esta_vacia() else 'No'}")

        elif op == "C":
            agregados = 0
            for pasajero in datos_prueba():
                if pila.apilar(pasajero):
                    agregados += 1
            print(f"  Cargados: {agregados}. Total en pila: {pila.longitud()}.")

        elif op == "0":
            break

        else:
            print("  Opción no válida.")


# -------------------- MENÚ 2: COLA --------------------

def menu_cola():
    while True:
        mostrar_opciones("MENÚ 2 · COLA (FIFO)", "Encolar", "Desencolar", "Ver frente")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if cola.encolar(pasajero):
                print("  Pasajero encolado correctamente.")

        elif op == "2":
            cola.listar()

        elif op == "3":
            pasajero = cola.desencolar()
            if pasajero is None:
                print("  La cola está vacía.")
            else:
                print(f"  Salió: {pasajero}")

        elif op == "4":
            pasajero = cola.ver_frente()
            if pasajero is None:
                print("  La cola está vacía.")
            else:
                print(f"  Frente: {pasajero}")

        elif op == "5":
            numero = leer_entero("  Número a buscar: ")
            posicion = cola.buscar(numero)
            if posicion == -1:
                print("  No existe ese pasajero.")
            else:
                print(f"  Encontrado en [{posicion}]: {cola.datos[posicion]}")

        elif op == "6":
            numero = leer_entero("  Número a modificar: ")
            destino = leer_texto("  Nuevo destino: ")
            asiento = leer_texto("  Nuevo asiento: ").upper()
            if cola.modificar(numero, destino, asiento):
                print("  Pasajero modificado correctamente.")
            else:
                print("  No existe ese pasajero.")

        elif op == "7":
            numero = leer_entero("  Número a eliminar: ")
            if cola.eliminar_por_numero(numero):
                print("  Pasajero eliminado correctamente.")
            else:
                print("  No existe ese pasajero.")

        elif op == "8":
            copia = cola.copiar()
            print("  Copia de la cola:")
            copia.listar()

        elif op == "9":
            print(f"  Longitud: {cola.longitud()}")
            print(f"  ¿Está vacía?: {'Sí' if cola.esta_vacia() else 'No'}")

        elif op == "C":
            agregados = 0
            for pasajero in datos_prueba():
                if cola.encolar(pasajero):
                    agregados += 1
            print(f"  Cargados: {agregados}. Total en cola: {cola.longitud()}.")

        elif op == "0":
            break

        else:
            print("  Opción no válida.")


# -------------------- MENÚ PRINCIPAL --------------------

def main():
    while True:
        print("\n===== TAREA PILAS Y COLAS · PASAJEROS =====")
        print("1. Menú 1 · Pila")
        print("2. Menú 2 · Cola")
        print("3. Salir")
        op = input("Opción: ").strip()

        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
