# PROBLEMA 03
def cargar_alumnos():
    alumnos = []
    print(" CARGA DE ALUMNOS ")
    
    while True:
        try:
            n = int(input("¿Cuántos alumnos desea ingresar?: "))
            if n > 0:
                break
            else:
                print("Debe ingresar un número mayor que cero.")
        except ValueError:
            print("Debe ingresar un número entero válido.")
    #ingresamos los datos de los alumnos
    for i in range(n):
        print(f"Alumno {i+1}:")
        nombre = input("Ingrese el nombre completo: ")
        
        notas = []
        for j in range(3):
            while True:
                try:
                    nota = float(input(f"Ingrese la nota {j+1} (0 a 10): "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("La nota debe estar entre 0 y 10.")
                except ValueError:
                    print(" Ingrese un número válido.")
        
        alumno = {"nombre": nombre, "notas": notas}
        alumnos.append(alumno)
    
    return alumnos

lista_alumnos = cargar_alumnos()
print(" LISTADO DE ALUMNOS ")
for alumno in lista_alumnos:
    print(f"Nombre: {alumno['nombre']}, Notas: {alumno['notas']}")

# PROBLEMA 04

# Clase base
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho


# Clase hija (hereda de Rectangulo)
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        # Un cuadrado es un rectángulo con lados iguales
        super().__init__(lado, lado)


# Programa principal para probar las clases
if __name__ == "__main__":
    print(" RECTÁNGULO ")
    largo = float(input("Ingrese el largo del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    rect = Rectangulo(largo, ancho)
    print(f"Área del rectángulo: {rect.calcular_area()}")

    print("CUADRADO")
    lado = float(input("Ingrese el lado del cuadrado: "))
    cuad = Cuadrado(lado)
    print(f"Área del cuadrado: {cuad.calcular_area()}")

# PROBLEMA 05

def evaluar_alumnos(lista_alumnos):
    aprobados = 0
    desaprobados = 0

    for alumno in lista_alumnos:
        promedio = sum(alumno["notas"]) / len(alumno["notas"])
        if promedio >= 4:
            aprobados += 1
        else:
            desaprobados += 1

    return aprobados, desaprobados

if __name__ == "__main__":
    # Lista de prueba (puedes usar cargar_alumnos del problema 3)
    alumnos = [
        {"nombre": "Ana", "notas": [5, 7, 6]},
        {"nombre": "Luis", "notas": [2, 3, 1]},
        {"nombre": "Carla", "notas": [4, 4, 5]},
    ]

    aprob, desaprob = evaluar_alumnos(alumnos)
    print(f"Alumnos aprobados: {aprob}")
    print(f"Alumnos desaprobados: {desaprob}")    

# PROBLEMA 06

def cargar_alumnos():
    alumnos = []
    print("=== CARGA DE ALUMNOS ===")
    
    while True:
        try:
            n = int(input("¿Cuántos alumnos desea ingresar?: "))
            if n > 0:
                break
            else:
                print("Debe ingresar un número mayor que cero.")
        except ValueError:
            print("Debe ingresar un número entero válido.")
    
    for i in range(n):
        print(f"\nAlumno {i+1}:")
        nombre = input("Ingrese el nombre completo: ")
        
        notas = []
        for j in range(3):
            while True:
                try:
                    nota = float(input(f"Ingrese la nota {j+1} (0 a 10): "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("⚠ La nota debe estar entre 0 y 10.")
                except ValueError:
                    print("⚠ Ingrese un número válido.")
        
        alumno = {"nombre": nombre, "notas": notas}
        alumnos.append(alumno)
    
    return alumnos


def promedio_curso(lista_alumnos):
    suma_total = 0
    cantidad_notas = 0
    
    for alumno in lista_alumnos:
        suma_total += sum(alumno["notas"])
        cantidad_notas += len(alumno["notas"])
    
    return suma_total / cantidad_notas if cantidad_notas > 0 else 0


# Programa principal
if __name__ == "__main__":
    alumnos = cargar_alumnos()
    
    print("\n=== LISTADO DE ALUMNOS ===")
    for alumno in alumnos:
        print(f"Nombre: {alumno['nombre']}, Notas: {alumno['notas']}")
    
    prom_curso = promedio_curso(alumnos)
    print(f"\nPromedio total del curso: {prom_curso:.2f}")

    # PROBLEMA 07


def cargar_alumnos():
    alumnos = []
    print("=== CARGA DE ALUMNOS ===")
    
    while True:
        try:
            n = int(input("¿Cuántos alumnos desea ingresar?: "))
            if n > 0:
                break
            else:
                print("Debe ingresar un número mayor que cero.")
        except ValueError:
            print("Debe ingresar un número entero válido.")
    
    for i in range(n):
        print(f"\nAlumno {i+1}:")
        nombre = input("Ingrese el nombre completo: ")
        
        notas = []
        for j in range(3):
            while True:
                try:
                    nota = float(input(f"Ingrese la nota {j+1} (0 a 10): "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("⚠ La nota debe estar entre 0 y 10.")
                except ValueError:
                    print("⚠ Ingrese un número válido.")
        
        alumno = {"nombre": nombre, "notas": notas}
        alumnos.append(alumno)
    
    return alumnos


def mejor_y_peor_promedio(lista_alumnos):
    if not lista_alumnos:
        return None, None

    mejor = lista_alumnos[0]
    peor = lista_alumnos[0]
    
    for alumno in lista_alumnos:
        promedio = sum(alumno["notas"]) / len(alumno["notas"])
        mejor_promedio = sum(mejor["notas"]) / len(mejor["notas"])
        peor_promedio = sum(peor["notas"]) / len(peor["notas"])
        
        if promedio > mejor_promedio:
            mejor = alumno
        if promedio < peor_promedio:
            peor = alumno
    
    return mejor, peor


# Programa principal
if __name__ == "__main__":
    alumnos = cargar_alumnos()
    
    print("\n=== LISTADO DE ALUMNOS ===")
    for alumno in alumnos:
        print(f"Nombre: {alumno['nombre']}, Notas: {alumno['notas']}")
    
    mejor, peor = mejor_y_peor_promedio(alumnos)
    
    if mejor and peor:
        prom_mejor = sum(mejor["notas"]) / len(mejor["notas"])
        prom_peor = sum(peor["notas"]) / len(peor["notas"])
        print(f"\n➡ El mejor promedio lo tiene {mejor['nombre']} con {prom_mejor:.2f}")
        print(f"➡ El peor promedio lo tiene {peor['nombre']} con {prom_peor:.2f}")

# PROBLEMA 07
# (Basado en el Problema 3)

def cargar_alumnos():
    alumnos = []
    print("=== CARGA DE ALUMNOS ===")
    
    while True:
        try:
            n = int(input("¿Cuántos alumnos desea ingresar?: "))
            if n > 0:
                break
            else:
                print("Debe ingresar un número mayor que cero.")
        except ValueError:
            print("Debe ingresar un número entero válido.")
    
    for i in range(n):
        print(f"\nAlumno {i+1}:")
        nombre = input("Ingrese el nombre completo: ")
        
        notas = []
        for j in range(3):
            while True:
                try:
                    nota = float(input(f"Ingrese la nota {j+1} (0 a 10): "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("⚠ La nota debe estar entre 0 y 10.")
                except ValueError:
                    print("⚠ Ingrese un número válido.")
        
        alumno = {"nombre": nombre, "notas": notas}
        alumnos.append(alumno)
    
    return alumnos


def buscar_alumno(lista_alumnos, busqueda):
    resultados = []
    busqueda = busqueda.lower()  # para hacer la búsqueda sin importar mayúsculas
    
    for alumno in lista_alumnos:
        if busqueda in alumno["nombre"].lower():
            promedio = sum(alumno["notas"]) / len(alumno["notas"])
            datos = {
                "nombre": alumno["nombre"],
                "notas": alumno["notas"],
                "promedio": round(promedio, 2)
            }
            resultados.append(datos)
    
    return resultados


# Programa principal
if __name__ == "__main__":
    alumnos = cargar_alumnos()
    
    print(" LISTADO DE ALUMNOS ")
    for alumno in alumnos:
        print(f"Nombre: {alumno['nombre']}, Notas: {alumno['notas']}")
    
    nombre_buscar = input("\nIngrese el nombre (o parte del nombre) del alumno a buscar: ")
    encontrados = buscar_alumno(alumnos, nombre_buscar)
    
    if encontrados:
        print(" RESULTADOS DE LA BÚSQUEDA ")
        for alum in encontrados:
            print(f"Nombre: {alum['nombre']}, Notas: {alum['notas']}, Promedio: {alum['promedio']}")
    else:
        print(" No se encontraron alumnos con ese nombre.")
