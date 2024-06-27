import json
from datetime import datetime

ventas = []

precios_pizzas = {
    "peperoni": {"pequeña": 5000, "mediana": 8000, "familiar": 10000},
    "mediterranea": {"pequeña": 6000, "mediana": 9000, "familiar": 12000},
    "vegetariana": {"pequeña": 5500, "mediana": 8500, "familiar": 11000}
}

def menu():
    print("\n--- Sistema de Ventas de Pizzas ---")
    print("1. Registrar una venta")
    print("2. Mostrar todas las ventas")
    print("3. Buscar ventas por cliente")
    print("4. Guardar las ventas en un archivo")
    print("5. Cargar las ventas desde un archivo")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def registrar_venta():
    nombre_cliente = input("Nombre del cliente: ")
    tipo_cliente = input("Tipo de cliente (diurno/vespertino/administrativo): ").lower()
    tipo_pizza = input("Tipo de pizza (peperoni/mediterranea/vegetariana): ").lower()
    tamaño_pizza = input("Tamaño de la pizza (pequeña/mediana/familiar): ").lower()
    
    if tipo_pizza not in precios_pizzas or tamaño_pizza not in precios_pizzas[tipo_pizza]:
        print("Tipo o tamaño de pizza inválido.")
        return
    
    precio = precios_pizzas[tipo_pizza][tamaño_pizza]
    
    descuento = 0
    if tipo_cliente == 'diurno':
        descuento = 0.15
    elif tipo_cliente == 'vespertino':
        descuento = 0.20
    elif tipo_cliente == 'administrativo':
        descuento = 0.10
    
    precio_final = precio * (1 - descuento)
    
    # Fecha y hora actual
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    venta = {
        "fecha_hora": fecha_hora,
        "nombre_cliente": nombre_cliente,
        "tipo_cliente": tipo_cliente,
        "tipo_pizza": tipo_pizza,
        "tamaño_pizza": tamaño_pizza,
        "precio_original": precio,
        "descuento": descuento,
        "precio_final": precio_final
    }
    ventas.append(venta)
    print(f"\nVenta registrada:\n")
    print(f"Fecha y hora: {fecha_hora}")
    print(f"Cliente: {nombre_cliente}")
    print(f"Tipo de cliente: {tipo_cliente}")
    print(f"Tipo de pizza: {tipo_pizza}")
    print(f"Tamaño de pizza: {tamaño_pizza}")
    print(f"Precio original: {precio}")
    print(f"Descuento aplicado: {descuento * 100}%")
    print(f"Precio final: {precio_final}")

def mostrar_ventas():
    if not ventas:
        print("No hay ventas registradas.")
    else:
        for venta in ventas:
            print(venta)

def buscar_ventas():
    nombre_cliente = input("Ingrese el nombre del cliente a buscar: ")
    ventas_cliente = [venta for venta in ventas if venta["nombre_cliente"] == nombre_cliente]
    
    if not ventas_cliente:
        print(f"No se encontraron ventas para el cliente {nombre_cliente}.")
    else:
        for venta in ventas_cliente:
            print(venta)

def guardar_ventas():
    with open('ventas.json', 'w') as file:
        json.dump(ventas, file, indent=4)
    print("Ventas guardadas en 'ventas.json'.")

def cargar_ventas():
    global ventas
    try:
        with open('ventas.json', 'r') as file:
            ventas = json.load(file)
        print("Ventas cargadas desde 'ventas.json'.")
    except FileNotFoundError:
        print("No se encontró el archivo 'ventas.json'.")

def main():
    while True:
        opcion = menu()
        if opcion == '1':
            registrar_venta()
        elif opcion == '2':
            mostrar_ventas()
        elif opcion == '3':
            buscar_ventas()
        elif opcion == '4':
            guardar_ventas()
        elif opcion == '5':
            cargar_ventas()
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

