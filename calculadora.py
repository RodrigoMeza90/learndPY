def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
      return a / b

print("¡Bienvenido a la calculadora básica!")


while True:   
    print("\nOpciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Seleccione una opcion")

    if opcion == '5':
        print("Saliendo de la calculadora")
        break

    num1 = float(input("ingrese el primer numero: "))
    num2 = float(input("seleccione el segundo numero: ")) 

    if opcion == '1':
        print(f"resultado: {sumar(num1, num2)}")
    elif opcion == '2':
        print(f"resultado: {restar(num1, num2)}")
    elif opcion == '3':
        print(f"resultado: {multiplicar(num1, num2)}") 
    elif opcion == '4':
        print(f"resultado: {dividir(num1, num2)}") 
    else:
        print("opcion no valida")

