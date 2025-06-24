import libreria.matematicas as mat

print('Operaciones')
print('1. Suma')
print('2. Resta')
print('3. Multiplicacion')
print('4. Division')

opcion = input('Seleccione una opcion 1, 2, 3 o 4:  ')
op1 = float(input('Ingrese un numero: '))
op2 = float(input('Ingrese un numero: '))

match opcion:
    case "1":
        r = mat.suma(op1, op2)
    case "2":
        r = mat.resta(op1, op2)
    case "3":
        r = mat.multiplicacion(op1, op2)
    case "4":
        r = mat.division(op1, op2)

print(f'El resultado de la operacion: {r:.2f}') 