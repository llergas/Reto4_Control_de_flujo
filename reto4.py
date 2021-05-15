import random
from  time import time
file = open("BD/Banco de Preguntas - Hoja 1.csv", "r", encoding="utf8")

lista_preguntas = []
for renglon in file:
    lista = renglon.split(",")
    lista_preguntas.append(lista)
print(lista_preguntas)
nivel = int(input("Ingrese el nivel que desea jugar: "))
ciclo = 0
puntaje = 0
acierto = 0
ayuda = 2
tiempo = 0

while True:

    tiempo_inicial = time()
    listaOpciones = ["a.", "b.", "c.", "d.", "?."]
    alea = random.randint(1, 22)


    print(lista_preguntas[alea][1])

    for i in range(2, 7):
        print(listaOpciones[i-2], lista_preguntas[alea][i])
    print()
    respuesta = input("Ingrese su respuesta o utiliza una ayuda a, b, c, d ó ? ").upper()


    if respuesta == lista_preguntas[alea][6]:
        print("Su respuesta es correcta")
        acierto += 1
    else:
        print("Su respeusta es Incorrecta")

    ciclo += 1
    tiempo_final = time() - tiempo_inicial
    tiempo += tiempo_final

    if nivel == 1 and ciclo == 2:
        break
    elif nivel == 2 and ciclo == 4:
        break
    elif nivel == 3 and ciclo == 6:
        break

if nivel == 1 and acierto == 2:
    puntaje = 200
else:
    puntaje = acierto * 50
if nivel == 2 and acierto == 4:
    puntaje = 500
else:
    puntaje = acierto * 50
if nivel == 3 and acierto == 6:
    puntaje = 1000
else:
    puntaje = acierto * 50

print(f"tiempo total {tiempo}")

if tiempo >= 60:
    print(f"Su puntaje final es {puntaje}")
else:
    print(f"Su puntaje final es {puntaje + (acierto * 35)}")

