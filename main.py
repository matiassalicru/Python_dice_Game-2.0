import random

# 3 dados
# 2 jugadores
# 2 rondas

# Si todos los dados son iguales -> suma 6 puntos

# Si 2 dados son iguales -> relanza el que es distinto

# Si los dados son todos distintos -> 0 puntos

# CREAR MENU DE OPCIONES PARA VER SI LA PERSONA QUIERE SEGUIR JUGANDO
print('/' * 79)
print('Bienvenidos al juego de dados')
print('/' * 79)


# FUNCIONES
def hubo_empates(puntaje1, puntaje2):  # Determina si hubo empates
    if puntaje1 == puntaje2:
        return True
    else:
        return False


def porcentaje_aciertos(aciertos, total):
    return aciertos * 100 / total


# ENTRADA Y DECLARACIÓN DE DATOS Y VARIABLES

nombre_1 = input('> Ingrese el nombre de el jugador 1: ')
nombre_2 = input('> Ingrese el nombre de el jugador 2: ')

puntaje_1, puntaje_2 = 0, 0  # Puntajes iniciales para jugadores 1 y 2

jugadas = 0  # Cantidad de veces que se tiran los dados (incluye ambos jugadores)
empates = 0  # Cantidad de enpates que se obtubieron en cada jugada
cont_puntaje_1, cont_puntaje_2 = 0, 0  # Contador de puntos para el promedio jugador 1/2
acierto1, acierto2 = 0, 0  # Cantidad de aciertos del jugador 1/2
porcentaje_aciertos1, porcentaje_aciertos2 = 0, 0  # Porcentaje de aciertos del jugador 1/2

ganadas_1 = 0
ganadas_2 = 0
hasWon3Times = False


puntuacion_objetivo = 0
while puntuacion_objetivo < 10:
    puntuacion_objetivo = int(input('> Ingrese la puntuación objetivo (debe ser mayor a 10): '))

# ------------------- PRESENTACIÓN -------------------------

print('-' * 79)

print('Comienza la ronda!')

print('Las reglas: si la suma de los 3 dados resulta la paridad elegida, entonces se te sumará el valor \n '
      'del dado mayor, y si además todos los dados son de la paridad elegida duplicas tus puntos!!  \n En caso de que'
      ' no aciertes a la paridad, se te restará el dado de menor valor :(')

print('-' * 79)

isMayor = False

while not isMayor:
    # ----------------- JUGADOR 1 ------------------
    print('Elija la paridad a la que apostarle')
    eleccion_paridad = str(input(f'> {nombre_1}, presione P para elegir par o I para elegir impar: ')).lower()

    print('-' * 79)
    input(f'> {nombre_1} presiona enter para tirar los dados')
    print('-' * 79)

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    dado3 = random.randint(1, 6)

    print('Sacaste: ', dado1, dado2, dado3)

    # Proceso de verificación de paridad elegida

    if eleccion_paridad == 'p':
        print('Elegiste par')

        if (dado1 + dado2 + dado3) % 2 == 0:
            print('La suma de los tres dados es par!')
            print('-' * 79)
            dado_mayor = max(dado1, dado2, dado3)
            puntaje_1 += dado_mayor
            print('El dado mayor fue: ', dado_mayor)
            print('Ahora tus puntos son: ', puntaje_1)
            print('-' * 79)
            acierto1 += 1

            if dado1 % 2 == 0 and dado2 % 2 == 0 and dado3 % 2 == 0:
                print('Puntaje actual', puntaje_1)
                print('Como ADEMÁS todos los dados que tiraste también fueron par! Así que duplicas tus puntos!!!')
                puntaje_1 *= 2
                print('Puntaje duplicado: ', puntaje_1)

        else:
            dado_menor = min(dado1, dado2, dado3)
            puntaje_1 -= dado_menor
            print('No salio la paridad elegida, tus puntos quedan en: ', puntaje_1)
            print('-' * 79)

    elif eleccion_paridad == 'i':
        print('elegiste impar')

        if (dado1 + dado2 + dado3) % 2 == 1:
            print('La suma de los tres dados es impar!')
            print('-' * 79)
            dado_mayor = max(dado1, dado2, dado3)
            puntaje_1 += dado_mayor
            print('El dado mayor fue: ', dado_mayor)
            print('Ahora tus puntos son: ', puntaje_1)
            print('-' * 79)
            acierto1 += 1

            if dado1 % 2 == 1 and dado2 % 2 == 1 and dado3 % 2 == 1:
                print('Puntaje actual', puntaje_1)
                print('Como ADEMÁS todos los dados que tiraste también fueron impar! Así que duplicas tus puntos!!!')
                puntaje_1 *= 2
                print('Puntaje duplicado: ', puntaje_1)
                print('-' * 79)

        else:
            dado_menor = min(dado1, dado2, dado3)
            puntaje_1 -= dado_menor
            print('No salio la paridad elegida se te restó el dado de menor valor,\n'
                  ' tus puntos quedan en:', puntaje_1)
            print('-' * 79)

    cont_puntaje_1 += puntaje_1

    # ------------------ JUGADOR 2 ------------------

    print(f'{nombre_2} Elija la paridad')
    eleccion_paridad = str(input(f'> {nombre_2}, presione P para elegir par o I para elegir impar: ')).lower()
    print('-' * 79)

    input(f'> {nombre_2} presiona enter para tirar los dados')
    print('-' * 79)

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    dado3 = random.randint(1, 6)

    print('Sacaste: ', dado1, dado2, dado3)

    # Proceso de verificación de paridad elegida
    if eleccion_paridad == 'p':
        print('Elegiste par')

        if (dado1 + dado2 + dado3) % 2 == 0:
            print('La suma de los tres dados es par!')
            print('-' * 79)
            dado_mayor = max(dado1, dado2, dado3)
            puntaje_2 += dado_mayor
            print('El dado mayor fue: ', dado_mayor)
            print('Tu nuevo puntaje es: ', puntaje_2)
            print('-' * 79)
            acierto2 += 1

            if dado1 % 2 == 0 and dado2 % 2 == 0 and dado3 % 2 == 0:
                print('Puntaje actual', puntaje_2)
                print('Como ADEMÁS todos los dados que tiraste también fueron par! Así que duplicas tus puntos!!!')
                puntaje_2 *= 2
                print('Puntaje duplicado: ', puntaje_2)
                print('-' * 79)

        else:
            dado_menor = min(dado1, dado2, dado3)
            puntaje_2 -= dado_menor
            print('No salió la paridad elegida, tus puntos quedan en: ', puntaje_2)
            print('-' * 79)

    elif eleccion_paridad == 'i':

        print('Elegiste impar')
        if (dado1 + dado2 + dado3) % 2 == 1:
            print('La suma de los tres dados es impar!')
            print('-' * 79)
            dado_mayor = max(dado1, dado2, dado3)
            puntaje_2 += dado_mayor
            print('El mayor fue: ', dado_mayor)
            print('Tu nuevo puntaje es: ', puntaje_2)
            print('-' * 79)
            acierto2 += 1
            if dado1 % 2 == 1 and dado2 % 2 == 1 and dado3 % 2 == 1:
                print('Puntaje actual', puntaje_2)
                print('Como ADEMÁS todos los dados que tiraste también fueron impar! Así que duplicas tus  puntos!!!')
                puntaje_2 *= 2
                print('Puntaje duplicado: ', puntaje_2)

        else:
            dado_menor = min(dado1, dado2, dado3)
            puntaje_2 -= dado_menor
            print('No salio la paridad elegida se te restó el dado de menor valor,\n'
                  ' tus puntos quedan en:', puntaje_2)

    if puntaje_1 > puntuacion_objetivo or puntaje_2 > puntuacion_objetivo:
        isMayor = True

    cont_puntaje_2 += puntaje_2

    # Comprueba el ganador de la ronda actual.
    if puntaje_1 != puntaje_2:
        if puntaje_1 > puntaje_2:
            ganadas_2 = 0
            ganadas_1 += 1
        else:
            ganadas_1 = 0
            ganadas_2 += 1
        if ganadas_1 >= 3 or ganadas_2 >= 3:
            hasWon3Times = True

    jugadas += 1
    print(f'----------------TERMINO LA JUGADA {jugadas}-----------------')

    empates = hubo_empates(puntaje_1, puntaje_2)


promedio_1 = round(cont_puntaje_1 / jugadas, 2)
promedio_2 = round(cont_puntaje_2 / jugadas, 2)
porcentaje_aciertos1 = round((porcentaje_aciertos(acierto1, jugadas)), 2)
porcentaje_aciertos2 = round((porcentaje_aciertos(acierto2, jugadas)), 2)

print('-' * 79)
if puntaje_1 > puntaje_2:
    print('Ganaste', nombre_1)
    if porcentaje_aciertos1 > porcentaje_aciertos2:
        print("Además tuviste el mayor porcentaje de aciertos: ", porcentaje_aciertos1, "%.")
elif puntaje_2 > puntaje_1:
    print('Ganaste', nombre_2)
    if porcentaje_aciertos2 > porcentaje_aciertos1:
        print("Además tuviste el mayor porcentaje de aciertos: ", porcentaje_aciertos2, "%.")
else:
    print('Hubo un empate, lo vas a dejar así?')

print('-' * 79)
print('Estadisticas: ')
print(f'\t Cantidad de jugadas: {jugadas}')
if empates:
    print(f"\t Hubo al menos un empate, lo vas a dejar asi!!?")
else:
    print("\t No hubo empates.")
print(f'\t El promedio de los puntajes del jugador {nombre_1} es {promedio_1}.')
print(f'\t El promedio de los puntajes del jugador {nombre_2} es {promedio_2}.')

print("\t El porcentaje de aciertos de ", nombre_1, "es: ", porcentaje_aciertos1, "%.")
print("\t El porcentaje de aciertos de ", nombre_2, "es: ", porcentaje_aciertos2, "%.")

if hasWon3Times:
    print('\t Uno de los jugadores ganó al menos 3 rondas seguidas')
else:
    print('\t NO hubo jugadores que ganaran al menos 3 rondas seguidas')

print('/' * 79)
print('Fin del juego')
print('/' * 79)

