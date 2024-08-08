nombre1 = input("¿Cómo se llama el jugador 1?: ")
nombre2 = input("¿Cómo se llama el jugador 2?: ")


#Queda pendiente colocar el nombre del jugador 1 y 2 y ver lo de las minusculas sumado al bucle

jugador1 = input ("¡Hola jugador1 ¿Qué elegis: Piedra, papel o tijera?: ")
jugador2 = input ("¡Hola jugador2 ¿Qué elegis: Piedra, papel o tijera?: ")



condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijera" and jugador2 =="papel"

if jugador1 == jugador2:
    print ("¡Ha sido un empate!")

elif condicion1 or condicion2 or condicion3:
    print ("Ha ganado: ", nombre1)

else:
    print ("Ha ganado: ", nombre2)

