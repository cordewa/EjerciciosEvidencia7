#Ejercicio de Estructuras Condicionales y Repetitivas
#Pidiendo al usuario que ingrese un numero
numero = int(input("Por favor Ingrese un numero: "))
if numero == 10:
    print("¡Usted ha ganado el sorteo!")

#Si numero es menor o si es mayor
numero = int(input("Ingrese un numero: "))
if numero == 10:
    print("Usted ha ganado el sorteo!")
elif numero < 10:
    print("¡Falto un poco, segui participando!")
else:
    print("¡Te pasaste, a seguir intentando!")


#Pedir al usuario que ingrese un dia a la semana
diasemana = input(" Por favor Ingrese un dia de la semana: ")
if diasemana.lower() == "lunes":
    print("Feliz lunes")
elif diasemana.lower() == "viernes":
    print("Feliz viernes")
elif diasemana.lower() == "sabado" or diasemana.lower() == "domingo":
        print("Feliz Finde")
else:
    print("No ingresaste un dia de semana")
    

#Ingresar letra
ingresarletra = input("Ingrese por favor una letra: ")
if ingresarletra.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Es una vocal")