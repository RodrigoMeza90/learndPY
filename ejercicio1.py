import random

numero_secreto = random.randint(1, 100)
max_intentos = 7
intentos = 0

print("bienvenido al juego de la adivinanza he pensando en un numero y debes de adivinar cual es en solo 3 intentos")

while intentos < max_intentos:
    adivinanza = int(input("ingresa tu adivinanza: "))
    intentos += 1
    if numero_secreto < adivinanza:
        print("tu adivinanza es mayor que el numero secreto")
    elif numero_secreto > adivinanza:
        print("tu adivinanza es menor que el numero secreto")
    else:
        print("felicidades acertaste")
        break
if intentos == max_intentos:
    print("superaste el numero de intentos, el numero secreto era: ", numero_secreto)