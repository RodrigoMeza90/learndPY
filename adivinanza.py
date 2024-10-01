import random

numero_secreto = random.randint(1, 100)

intentos = 0

print("Adivine el numero entre 1 y 100")

while True:
    adivinanza = int(input("ingrese tu adivinanza: "))
    intentos += 1
    if adivinanza > numero_secreto:
        print("el numero es menor que", adivinanza)
    elif adivinanza < numero_secreto:
        print("el numero es mayor que", adivinanza)
    else:
        print(f"Felicidades adivinaste el numero en {intentos} intento")
        break

