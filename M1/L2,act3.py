import random

numero = random.randint(1,20)
print("tienes 5 intentos para adivinar un numero del 1 al 20")
for i in range(5):
    f = int(input("escribe un numero entre el 1 y el 20:"))
    if f > numero:
        print("el numero es menor")
    elif f < numero:
        print("el numero es mayor")
    else:
        print("felicitaciones es el numero correcto, el numero es", numero)
        break