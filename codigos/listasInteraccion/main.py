puntosIni = 2000


#def valiarAtributo(vida, defensa, agilidad, fuerza,)


def validarInput(atributo ,puntosIni):
    while True:
        try:
            valor = int(input(f"Ingrese el valor de {atributo} del jugador: "))

            if valor <= puntosIni:
                return valor  #valor valido
            else:
                print(f"El valor ingresado para {atributo} supera los puntos iniciales disponibles ({puntosIni}). Intente de nuevo.")
        except ValueError:
            print("Entrada de atributo no valida)")


print(f"Tienes {puntosIni} puntos iniciales para distribuir en tus atributos.")

#obtener la vida del jugador

vida = validarInput("vida", puntosIni)
print("-" * 30)
puntosIni -= vida 
print(f"Puntos iniciales restantes: {puntosIni}")
print("-" * 30)


defensa = validarInput("defensa", puntosIni)
print("-" * 30)
puntosIni -= defensa
print(f"Puntos iniciales restantes: {puntosIni}")
print("-" * 30)



agilidad = validarInput("agilidad", puntosIni)
print("-" * 30)
puntosIni -= agilidad
print(f"Puntos iniciales restantes: {puntosIni}")
print("-" * 30)



fuerza = validarInput("fuerza", puntosIni)
print("-" * 30)
puntosIni -= fuerza
print(f"Puntos iniciales restantes: {puntosIni}")
print("-" * 30)



suerte = validarInput("suerte", puntosIni)
print("-" * 30)
puntosIni -= suerte
print(f"Puntos iniciales restantes: {puntosIni}")
print("-" * 30)



magia = validarInput("magia", puntosIni)
print("-" * 30)
puntosIni -= magia
print(f"Puntos iniciales restantes: {puntosIni}")
print("-" * 30)

nivel = 1
experiencia = 0
exoeriencia_Up = 10
puntosSubida = 1

personaje = [vida,"<-HP", defensa,"<-DF",agilidad,"<-AG",fuerza,"<-ST",suerte,"<-LU",magia,"<-MA"]

print("Su personaje")
print(*personaje)


vidaEnemigo = 1000
defensaEnemigo = 200
agilidadEnemigo = 50
magiaEnemigo = 100
fuerzaEnemigo = 150
suerteEnemigo = 50

enemigo = [vidaEnemigo, "<-HP", defensaEnemigo, "<-DF", agilidadEnemigo, "<-AG", fuerzaEnemigo, "<-ST", suerteEnemigo, "<-LU", magiaEnemigo, "<-MA"]
print("El enemigo")
print(*enemigo)

print("combate")

while vida > 0 and vidaEnemigo > 0:
    print("Turno del jugador")
    ataque = fuerza + magia
    print(f"El jugador ataca con {ataque} de daño.")

    if suerte > suerteEnemigo:
        print("¡Ataque crítico!")
        ataque *= 2
        suerte -= 10  # reducir la suerte del jugador si el ataque es crítico
    else:
        print("Ataque normal.")
        suerte += 10  # incrementar la suerte del jugador si no es crítico


    if agilidad > agilidadEnemigo:
        vidaEnemigo -= ataque
        print(f"La vida del enemigo es ahora: {vidaEnemigo}")
        agilidad -= 10  # reducir la agilidad del jugador si el ataque es exitoso
    else:
        print("El ataque del jugador falla debido a la agilidad del enemigo.")
        agilidad += 10 #incrementar la agilidad del jugador si falla el ataque

    if vidaEnemigo <= 0:
        print("¡El enemigo ha sido derrotado!")
        break

    print("Turno del enemigo")
    ataqueEnemigo = fuerzaEnemigo + magiaEnemigo

    if suerteEnemigo > suerte:
        print("¡Ataque crítico del enemigo!")
        ataqueEnemigo *= 2
        suerteEnemigo -= 10
    else:
        print("Ataque normal del enemigo.")
        suerteEnemigo += 10

    if agilidadEnemigo > agilidad:
        print(f"El enemigo ataca con {ataqueEnemigo} de daño.")
        vida -= ataqueEnemigo
        print(f"La vida del jugador es ahora: {vida}")
        agilidadEnemigo -= 10
    else:
        print("El ataque del enemigo falla debido a la agilidad del jugador.")
        agilidadEnemigo += 10

    if vida <= 0:
        print("¡El jugador ha sido derrotado!")
        break

print("Fin del combate")













































