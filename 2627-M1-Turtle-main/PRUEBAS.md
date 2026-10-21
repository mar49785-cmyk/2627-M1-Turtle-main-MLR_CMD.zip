# Comprobaciones visibles de M1

Ejecuta el juego después de cada cambio y anota el resultado:

- ambas velocidades positivas: termina y anuncia una ganadora;
    
    Configuración: RED_SPEED = 4.5 // BLUE_SPEED = 5.5
    
    Predicción: La tortuga azul ganará porque si velocidad es mayor que la de la tortuga roja.
    
    Resultado: El código ha validado que ambas son mayores a 0 e inicia el bucle. La azul cruza primero la meta y se muestra en la ventana que ha ganado la tortuga azul.


- roja más rápida: gana la roja;

    Configuración: RED_SPEED = 7 // BLUE_SPEED = 3
    
    Predicción: Gana la roha porque avanza 7 píxeles frente a los 3.
    
    Resultado: red_finished se activa primero, la función devuelve roja y el título indica que ha ganado la roja


- azul más rápida: gana la azul;

    Configuración: RED_SPEED = 2 // BLUE_SPEED = 3

    Predicción: Gana la azul por una diferencia considerable de velocidad.

    Resultado: La tortuga azul llega antes a la meta, devolviendo "azul" y actualizando correctamente el título en la ventana.


- velocidades iguales: anuncia un empate (no puede ganar siempre la roja);

    Configuración: RED_SPEED = 5 // BLUE_SPEED = 5

    Predicción: Habrá un empate, ya que ambas avanzan exactamente la misma cantidad de píxeles y parten de la misma posición inicial.

    Resultado: En el instante en el que superan FINISH_X, tanto red_finished como blue_finiched son True a la vez. El código evalúa if red_finiched and blue_finished: y devuelve "empate", por lo que en la ventana se miuestra la linea de empate y que las dos tortugas llegan a la vez.


- alguna velocidad igual a cero o negativa: muestra el aviso y no inicia la carrera;

    Configuración: RED_SPEED = 0 y -3 (vamos a hacer 2 pruebas) // BLUE_SPEED = 3

    Predicción: No debe de iniciarse la carrera y debe de mostrarse un mensaje de error en la consola y detenerse.

    Resultado: El consicional de validación que pusimos en el código detecta que el valor no es válido e imprime el aviso por consola, ejecuta el return "" y frena la ejecución sin colgarse ni arrancar el bucle gráfico.

- antes de ejecutar, puedes justificar tu predicción usando las velocidades.

No se considera terminado si sólo funciona con una combinación concreta.
