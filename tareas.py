
import heapq

# Cola de prioridad vacía
cola_prioridad = []

# Diccionario para convertir texto a prioridad numérica
# Se usa un arreglo, ya que se tiene definido el tamaño del arreglo
prioridad_valores = {"Alta": 1, "Media": 2, "Baja": 3}

def agregar_tarea(): # Inicializamos una lista vacía que actuará como nuestra cola de prioridad. Usaremos la función heapq.heappush para insertar tareas en esta lista y ordenarlas automáticamente por su prioridad.
    """AGREGAR UNA NUEVA TAREA A LA COLA DE PRIORIDAD."""
    tarea = input("Ingrese la tarea: ")
    prioridad_texto = input("Ingrese la prioridad (Alta, Media, Baja): ").capitalize()
    
    if prioridad_texto not in prioridad_valores:
        print("Prioridad no válida. Use Alta, Media o Baja.")
        return

    prioridad = prioridad_valores[prioridad_texto]
    heapq.heappush(cola_prioridad, (prioridad, tarea))
    print(f"Tarea '{tarea}' con prioridad {prioridad_texto} agregada.")

def procesar_tarea():
    """Procesa la tarea más urgente (con mayor prioridad)."""
    if cola_prioridad:
        prioridad, tarea = heapq.heappop(cola_prioridad)
        print(f"Procesando tarea: {tarea} (Prioridad: {prioridad})")
    else:
        print("No hay tareas pendientes.")

def mostrar_tareas():
    """Muestra la lista de tareas pendientes ordenadas por prioridad."""
    if not cola_prioridad:
        print("No hay tareas pendientes.")
        return

    print("\nLista de tareas pendientes:")
    for prioridad, tarea in sorted(cola_prioridad):
        prioridad_texto = [k for k, v in prioridad_valores.items() if v == prioridad][0]
        print(f"- {tarea} (Prioridad: {prioridad_texto})")

def menu():
    """Menú interactivo para gestionar tareas."""
    while True:
        print("\nMenú:")
        print("1. Agregar nueva tarea")
        print("2. Procesar tarea más urgente")
        print("3. Mostrar lista de tareas")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            procesar_tarea()
        elif opcion == "3":
            mostrar_tareas()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el menú principal
if __name__ == "__main__":
    menu()
