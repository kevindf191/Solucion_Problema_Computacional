# Sistema de facturación y análisis de ventas de trajes

# --- Declaración e Inicialización de Arreglos Unidimensionales ---

# Estos arreglos almacenarán la información de cada cliente, manteniendo la correspondencia por índice.
nombres_clientes = []          # Almacena el nombre de cada cliente
apellidos_clientes = []        # Almacena el apellido de cada cliente
cantidades_trajes = []         # Almacena la cantidad de trajes comprados por cada cliente
precios_unitarios = []         # Almacena el precio unitario del traje en la venta de cada cliente
totales_pagar = []             # Almacena el total final a pagar por cada cliente después del descuento

# Variable de control para el ciclo de registro de clientes
continuar_registro = True

# --- Ciclo principal para registrar múltiples clientes ---
while continuar_registro:
    print("\n--- Nuevo Registro de Cliente ---")

    # --- Entrada de Datos del Cliente ---
    nombre = input("Ingrese el nombre del cliente: ").strip()
    apellido = input("Ingrese el apellido del cliente: ").strip()

    # Validación para cantidad de trajes
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de trajes a comprar: "))
            if cantidad <= 0:
                print("La cantidad de trajes debe ser un número positivo. Intente de nuevo.")
            else:
                break 
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero para la cantidad.")

    # Validación para precio unitario
    while True:
        try:
            precio_unitario = float(input("Ingrese el precio unitario del traje: "))
            if precio_unitario <= 0:
                print("El precio unitario debe ser un número positivo. Intente de nuevo.")
            else:
                break 
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número para el precio.")

    # --- Cálculos de Subtotal, Descuento y Total ---
    
    subtotal = cantidad * precio_unitario
    descuento_porcentaje = 0.0 

    # Descuento según la cantidad de trajes
    if cantidad == 1:
        descuento_porcentaje = 0.10  
    elif cantidad == 2:
        descuento_porcentaje = 0.20 
    elif cantidad == 3:
        descuento_porcentaje = 0.40 
    elif cantidad > 3:
        descuento_porcentaje = 0.60 

    monto_descuento = subtotal * descuento_porcentaje
    total_a_pagar = subtotal - monto_descuento

    # --- Almacenamiento de Datos en los Arreglos ---
    nombres_clientes.append(nombre)
    apellidos_clientes.append(apellido)
    cantidades_trajes.append(cantidad)
    precios_unitarios.append(precio_unitario)
    totales_pagar.append(total_a_pagar)

    # --- Mostrar Resumen de la Compra Actual ---
    print("\n--- Resumen de la Compra ---")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento aplicado ({descuento_porcentaje * 100:.0f}%): ${monto_descuento:.2f}")
    print(f"Total a pagar: ${total_a_pagar:.2f}")

    # --- Preguntar al usuario si desea registrar otro cliente ---
    respuesta = input("\n¿Desea registrar otro cliente? (s/n): ").lower().strip()
    if respuesta != 's':
        continuar_registro = False # Cambia la variable de control para salir del ciclo

# --- Resumen Final de Todas las Ventas Registradas ---
print("\n--- RESUMEN GENERAL DE VENTAS ---")
if not nombres_clientes: # Verifica si la lista de clientes está vacía
    print("No se registraron ventas.")
else:
    # Itera sobre los arreglos usando el índice para mostrar cada registro completo
    for i in range(len(nombres_clientes)):
        print(f"\nCliente {i+1}:")
        print(f"  Nombre: {nombres_clientes[i]} {apellidos_clientes[i]}")
        print(f"  Cantidad de Trajes: {cantidades_trajes[i]}")
        print(f"  Precio Unitario: ${precios_unitarios[i]:.2f}")
        print(f"  Total Pagado: ${totales_pagar[i]:.2f}")

print("\n--- Fin del Programa ---")