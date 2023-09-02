# Juan Pablo Zapata Cano 

import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 10)
    intentos = 0

    print("¡Bienvenido a Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 10.")

    while True:
        try:
            guess = int(input("¿Cuál crees que es el número? "))
            intentos += 1

            if guess < numero_secreto:
                print("Demasiado bajo. Inténtalo de nuevo.")
            elif guess > numero_secreto:
                print("Demasiado alto. Inténtalo de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                break

        except ValueError:
            print("Por favor, ingresa un número válido.")

adivina_el_numero()