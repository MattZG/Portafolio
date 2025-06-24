#Modulo 2: Actividad de consolidiacion

#Eres contratado/a por una pequeña cadena de librerías llamada "Libros & Bytes" para desarrollar un sistema que gestione su inventario y permita a los usuarios simular una compra en línea. 
# Trabajarás solo en la lógica del sistema sin preocuparte de la interfaz visual. El sistema debe cumplir con los siguientes requerimientos y funcionalidades.

# 1 Definir variables básicas y tipos de datos:

inventario = [
    {'Título': 'Dune', 'Autor': 'Frank Herbert', 'Precio': 10.99, 'Stock': 4},
    {'Título': '1984', 'Autor': 'George Orwell', 'Precio': 6.99, 'Stock': 7},
    {'Título': 'El temor de un hombre sabio', 'Autor': 'Patrick Rothfuss', 'Precio': 22.99, 'Stock': 5},
    {'Título': 'El archivo de las tormentas', 'Autor': 'Brandon Sanderson', 'Precio': 16.99, 'Stock': 6},
    {'Título': 'Canción de hielo y fuego', 'Autor': 'George R.R. Martin', 'Precio': 20.99, 'Stock': 0}
]

#print(inventario)

#Salida:

#[{'Título': 'Dune', 'Autor': 'Frank Herbert', 'Precio': 10.99, 'Stock': 4}, 
# {'Título': '1984', 'Autor': 'George Orwell', 'Precio': 6.99, 'Stock': 7}, 
# {'Título': 'El temor de un hombre sabio', 'Autor': 'Patrick Rothfuss', 'Precio': 22.99, 'Stock': 5}, 
# {'Título': 'El archivo de las tormentas', 'Autor': 'Brandon Sanderson', 'Precio': 16.99, 'Stock': 6}, 
# {'Título': 'Canción de hielo y fuego', 'Autor': 'George R.R. Martin', 'Precio': 20.99, 'Stock': 0}]

#2 Control de flujo:

def mostrar_libros_disponibles():
    print('\nLibros disponibles con más de una unidad disponible: ')
    for libro in inventario:
        if libro['Stock'] > 1:
            print(f"{libro['Título']}, {libro['Autor']}, ${libro['Precio']}, Stock: {libro['Stock']}")

#mostrar_libros_disponibles()

#Salida:
# Libros disponibles con más de una unidad disponible:
# Dune, Frank Herbert, $10.99, Stock: 4
# 1984, George Orwell, $6.99, Stock: 7
# El temor de un hombre sabio, Patrick Rothfuss, $22.99, Stock: 5
# El archivo de las tormentas, Brandon Sanderson, $16.99, Stock: 6

# 3. Condiciones y operadores

def filtrar_precio():
    min = float(input('Ingrese el precio mínimo: '))
    max = float(input('Ingrese el precio máximo: '))

    libros_disponibles = []
    
    for libro in inventario:
            if min <= libro['Precio'] <= max:
                libros_disponibles.append(libro)
            
    if len(libros_disponibles) == 0:
        print('No hay libros disponibles dentro de tu presupuesto')
    else: 
        print(f'\nPuedes comprar estos libros: ')
        for libro in libros_disponibles:
            print(f"{libro['Título']}, {libro['Autor']}, ${libro['Precio']}, Stock: {libro['Stock']}")

#filtrar_precio()

# Salida:

#Ingrese el precio mínimo: 20
#Ingrese el precio máximo: 30

#Puedes comprar estos libros:
#El temor de un hombre sabio, Patrick Rothfuss, $22.99, Stock: 5
#Canción de hielo y fuego, George R.R. Martin, $20.99, Stock: 0

# 4. Función personalizada para simular una compra:

def comprar_libros(titulo, cantidad):
    for libro in inventario:
        if libro['Título'].lower() == titulo.lower():
            if libro['Stock'] >= cantidad:
                total = libro['Precio'] * cantidad
                libro['Stock'] -= cantidad
                print(f'\nCompra exitosa:')
                print(f"{cantidad} x {libro['Título']} = ${total:.2f}")
                return total 
            else:
                print(f"\nNo hay suficiente stock. Solo quedan {libro['Stock']} unidades de '{libro['Título']}'.")
                return None
    print(f"\nEl libro '{titulo}' no se encuentra en el inventario.")
    return None

#comprar_libros('Dune', 1)

#Salida:

#Compra exitosa:
#1 x Dune = $10.99

# 5. Uso de bucle while para iterar hasta que el usuario decida salir

def compras():
    while True:
        print('\n¡Bienvenido/a a Libros & Bytes!')
        print('\nSistema de compras')
        print('1. Mostrar libros disponibles.')
        print('2. Filtrar libros por rango de precios.')
        print('3. Comprar libros.')
        print('4. Finalizar la compra.')

        opcion = input('¿Qué desea hacer?: ')

        match opcion:
            case '1':
                mostrar_libros_disponibles()

            case '2':
                filtrar_precio()

            case '3':
                while True:
                    titulo = input("\nIngrese el título del libro a comprar (o escriba 'salir' para volver al menú): ")
                    if titulo.lower() == 'salir':
                        break

                    cantidad = input('Ingrese la cantidad: ')
                    if not cantidad.isdigit():
                        print('Por favor, ingrese una cantidad válida.')
                        continue
                    
                    cantidad = int(cantidad)
                    comprar_libros(titulo, cantidad)

            case '4':
                print('\nGracias por tu compra. ¡Hasta pronto!')
                break

            case _:
                print('Opción inválida. Intente nuevamente.')

#compras()

#Salida:

#¡Bienvenido/a a Libros & Bytes!

#Sistema de compras
#1. Mostrar libros disponibles.
#2. Filtrar libros por rango de precios.
#3. Comprar libros.
#4. Finalizar la compra.
#¿Qué desea hacer?: 1

#Libros disponibles con más de una unidad disponible:
#Dune, Frank Herbert, $10.99, Stock: 3
#1984, George Orwell, $6.99, Stock: 7
#El temor de un hombre sabio, Patrick Rothfuss, $22.99, Stock: 5
#El archivo de las tormentas, Brandon Sanderson, $16.99, Stock: 6

#¡Bienvenido/a a Libros & Bytes!

#Sistema de compras
#1. Mostrar libros disponibles.
#2. Filtrar libros por rango de precios.
#3. Comprar libros.
#4. Finalizar la compra.
#¿Qué desea hacer?: 2
#Ingrese el precio mínimo: 5   
#Ingrese el precio máximo: 15

#Puedes comprar estos libros:
#Dune, Frank Herbert, $10.99, Stock: 3
#1984, George Orwell, $6.99, Stock: 7

#¡Bienvenido/a a Libros & Bytes!

#Sistema de compras
#1. Mostrar libros disponibles.
#2. Filtrar libros por rango de precios.
#3. Comprar libros.
#4. Finalizar la compra.
#¿Qué desea hacer?: 3

#Ingrese el título del libro a comprar (o escriba 'salir' para volver al menú): Dune
#Ingrese la cantidad: 1

#Compra exitosa:
#1 x Dune = $10.99

#Ingrese el título del libro a comprar (o escriba 'salir' para volver al menú): 1984
#Ingrese la cantidad: 1

#Compra exitosa:
#1 x 1984 = $6.99

#Ingrese el título del libro a comprar (o escriba 'salir' para volver al menú): salir

#¡Bienvenido/a a Libros & Bytes!

#Sistema de compras
#1. Mostrar libros disponibles.
#2. Filtrar libros por rango de precios.
#3. Comprar libros.
#4. Finalizar la compra.
#¿Qué desea hacer?: 4

#Gracias por tu compra. ¡Hasta pronto!

# 6. Estructura de datos, gestión de descuentos

descuento_autor = {
    'Brandon Sanderson': 0.1,
    'Frank Herbert': 0.3
}

total_libros = 0
monto_total = 0.0
descuento_total = 0.0  

def comprar_libros(titulo, cantidad):
    global total_libros, monto_total, descuento_total
    
    for libro in inventario:
        if libro['Título'].lower() == titulo.lower():
            if cantidad <= libro['Stock']:
                autor = libro['Autor']
                precio_unidad = libro['Precio']
                subtotal = precio_unidad * cantidad

                descuento = descuento_autor.get(autor, 0)
                diferencia = subtotal * descuento
                total = subtotal - diferencia
                
                libro['Stock'] -= cantidad
                print(f'\nCompra exitosa:')
                print(f'{cantidad} x {libro['Título']} = ${total:.2f}')
                print(f'Descuento aplicado: {descuento * 100:.1f}%')

                total_libros += cantidad
                monto_total += total
                descuento_total += diferencia
                
                return total 
            else:
                print(f"\nNo hay suficiente stock. Solo quedan {libro['Stock']} unidades de '{libro['Título']}'.")
                return None
    print(f"\nEl libro '{titulo}' no se encuentra en el inventario.")
    return None

#comprar_libros('El archivo de las tormentas', 1)

#Salida:

#Compra exitosa:
#1 x El archivo de las tormentas = $15.29

#7. Simulación de una factura

def compras():
    global total_libros, monto_total, descuento_total
    
    while True:
        print('\n¡Bienvenido/a a Libros & Bytes!')
        print('\nSistema de compras:')
        print('1. Mostrar libros disponibles.')
        print('2. Filtrar libros por rango de precios.')
        print('3. Comprar libros')
        print('4. Finalizar la compra y emitir la factura.')

        opcion = input('Que desea hacer?: ')

        match opcion:
            case '1':
                mostrar_libros_disponibles()
            case '2':
                filtrar_precio()
            case '3':
                while True:
                    titulo = str(input("\nIngrese el título del libro a comprar (o escriba 'salir' para volver al menú): "))
                    if titulo.lower() == 'salir':
                        break

                    cantidad = input('Ingrese la cantidad: ')
                    if not cantidad.isdigit():
                        print('Por favor, ingrese una cantidad válida.')
                        continue
                    
                    cantidad = int(cantidad)
                    comprar_libros(titulo, cantidad)
            case '4':
                print('\nFACTURA FINAL')
                print(f'Total de libros comprados: {total_libros}')
                print(f'Monto total pagado: ${monto_total:.2f}')
                print(f'Ahorro total por descuentos: ${descuento_total:.2f}')
                print('\nGracias por tu compra. ¡Hasta pronto!')
                break
            case _:
                print('Opcion invalida. Intente nuevamente.')

compras()

# Salida:

#¡Bienvenido/a a Libros & Bytes!

#Sistema de compras:
#1. Mostrar libros disponibles.
#2. Filtrar libros por rango de precios.
#3. Comprar libros
#4. Finalizar la compra y emitir la factura.
#Que desea hacer?: 3

#Ingrese el título del libro a comprar (o escriba 'salir' para volver al menú): dune
#Ingrese la cantidad: 1

#Compra exitosa:
#1 x Dune = $7.69
#Descuento aplicado: 30.0%

#Ingrese el título del libro a comprar (o escriba 'salir' para volver al menú): 1984 
#Ingrese la cantidad: 2

#Compra exitosa:
#2 x 1984 = $13.98
#Descuento aplicado: 0.0%

#Ingrese el título del libro a comprar (o escriba 'salir' para volver al menú): salir

#¡Bienvenido/a a Libros & Bytes!

#Sistema de compras:
#1. Mostrar libros disponibles.
#2. Filtrar libros por rango de precios.
#3. Comprar libros
#4. Finalizar la compra y emitir la factura.
#Que desea hacer?: 4

#FACTURA FINAL
#Total de libros comprados: 3
#Monto total pagado: $21.67
#Ahorro total por descuentos: $3.30

#Gracias por tu compra. ¡Hasta pronto!