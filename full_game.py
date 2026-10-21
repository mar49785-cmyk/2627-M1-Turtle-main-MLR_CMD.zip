"""Primer hito: carrera de dos tortugas.

La infraestructura gráfica ya está resuelta. Los TODO sólo requieren variables,
condicionales y bucles, que son los contenidos impartidos al anunciar M1.
"""

from __future__ import annotations

import turtle


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
START_X = -320
FINISH_X = 300

# TODO 1: asigna dos velocidades positivas. Predice quién ganará.
RED_SPEED = 5
BLUE_SPEED = 5


def prepare_game():
    """Prepara la ventana, la pista y las dos tortugas (código proporcionado)."""
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title("Carrera de tortugas")

    painter = turtle.Turtle(visible=False)
    painter.speed(0)
    for y in (-80, 0, 80):
        painter.penup()
        painter.goto(START_X, y)
        painter.pendown()
        painter.forward(FINISH_X - START_X)

    red = turtle.Turtle(shape="turtle")
    red.color("red")
    red.penup()
    red.goto(START_X, 40)

    blue = turtle.Turtle(shape="turtle")
    blue.color("blue")
    blue.penup()
    blue.goto(START_X, -40)
    return screen, red, blue


def run_race(red, blue):
    """Mueve las tortugas hasta que una alcance la meta."""
    # TODO 2: valida con un condicional que ambas velocidades sean positivas.
    # Si alguna no lo es, muestra un mensaje y devuelve una cadena vacía.
    
    if RED_SPEED <= 0 or BLUE_SPEED <= 0:
        print("¡Error! Ambas velocidades deben de ser mayores a 0")
        return ""
    
    # EXPLICACIÓN
    # El condicional que hemos añadido verifica que al menos una de las velocidades es menor a 0
    # En caso de que esto ocurra, lanza un mensaje de eroor y detiene inmediatamente la funcion run_race
    # con la linea return ""

    # TODO 3: crea un bucle que mueva las dos tortugas en cada vuelta.
    # Cuando una alcance FINISH_X, devuelve "roja" o "azul".
    # Si las dos alcanzan FINISH_X en la misma vuelta, devuelve "empate".
    
    while True:
        red.forward(RED_SPEED)
        blue.forward(BLUE_SPEED)
        red_finished = red.xcor() >= FINISH_X
        blue_finished =blue.xcor() >= FINISH_X
        if red_finished and blue_finished:
            return "empate"
        elif red_finished:
            return "roja"
        elif blue_finished:
            return "azul"
    # EXPLICACIÓN:
    # Primero inicamos un bucle infinito que repetirá las instrucciones de su interior
    # una y otra vez hasta que alguna toruga gane y se ejecute un return.
    # Los color.forward hacen que las tortugas se muevan hacia delante la cantidad de píxeles 
    # indicada en su velocidad.
    # las lineas color_finished son para comprobar mediante el método xcor si la posición horizontal actual 
    # de la tortuga es mayor o igual a la linea de meta y se guarda mediante un True si llegó o False si no.
    # El bucle final simplemente indica el resultado de que tortuga llego a la meta en función del color_finished.

def main():
    """Pone en marcha la carrera (código proporcionado)."""
    screen, red, blue = prepare_game()
    winner = run_race(red, blue)
    if winner == "empate":
        screen.title("¡Empate! Las dos tortugas llegan a la vez")
    elif winner:
        screen.title(f"¡Ha ganado la tortuga {winner}!")
    screen.mainloop()


if __name__ == "__main__":
    main()
