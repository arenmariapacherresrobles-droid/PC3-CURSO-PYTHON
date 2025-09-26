# palabra reservada para seguir preguntando al usuario hasta que ingrese un valor correcto
while True: #mientras la condicion sea verdadera repite este bloque 
    try: #codigo que podria fallar 
        fraccion = input("Ingrese la fracción con formato (X/Y): ")
        x, y = fraccion.split("/")   # separar numerador y denominador
        x = int(x)
        y = int(y)
        if y == 0:   # no se puede dividir entre cero
            raise ZeroDivisionError
        if x > y:    # el numerador no puede ser mayor al denominador
            raise ValueError

        porcentaje = round((x / y) * 100)
#colocamos los casos del problema

        if porcentaje <= 1: #Colocar E en caso X/Y sea menor a 1% del total
            print("E")
        elif porcentaje >= 99: #Colocar F en caso X/Y sea mayor a 99%. 
            print("F")
        else:
            print(f"{porcentaje}%") #En otro caso, devolver el valor en porcentaje % 
        break   # salimos del bucle si todo sale bien
    
    except ValueError:
        print("❌ Error: Ingrese números enteros válidos y asegúrese de que X ≤ Y.")
    except ZeroDivisionError:
        print("❌ Error: El denominador no puede ser 0.")