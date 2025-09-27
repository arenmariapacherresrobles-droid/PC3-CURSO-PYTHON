# PROBLEMA 03
def cargar_alumnos():
    alumnos = []
    print("\nCargar alumnos:")
    while True:
        try:
            n = int(input("¿Cuántos alumnos desea ingresar?: "))
            if n >= 0:
                break
            else:
                print("Ingrese un número no negativo.")
        except ValueError:
            print("Debe ingresar un número entero válido.")
    for i in range(n):
        print(f"\nAlumno {i+1}: ")
        nombre = input("Ingrese nombre y apellidos del alumno: ")

        notas = []
        for j in range(3):
            while True:
                try:
                    nota = float(input(f"Ingrese la nota {j+1} (0-10): "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("La nota debe estar entre 0 y 10.")
                except ValueError:
                    print("Debe ingresar un número válido.")
        alumnos.append({"nombre": nombre, "notas": notas})

    return alumnos

# PROBLEMA 04
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

# PROBLEMA 05
def contar_aprobados(alumnos):
    if not alumnos:
        print("No hay alumnos cargados.")
        return
    aprobados = 0
    desaprobados = 0
    for alumno in alumnos:
        promedio = sum(alumno["notas"]) / len(alumno["notas"])
        if promedio >= 4:
            aprobados += 1
        else:
            desaprobados += 1
    print(f"\n✅ Aprobados: {aprobados}")
    print(f"❌ Desaprobados: {desaprobados}")

# PROBLEMA 06
def promedio_curso(alumnos):
    if not alumnos:
        print("No hay alumnos cargados.")
        return
    total_notas = 0
    cantidad_notas = 0
    for alumno in alumnos:
        total_notas += sum(alumno["notas"])
        cantidad_notas += len(alumno["notas"])
    promedio = total_notas / cantidad_notas if cantidad_notas > 0 else 0
    print(f"\n📊 Promedio general del curso: {promedio:.2f}")

# PROBLEMA 07a (mejor y peor) - ahora DEVUELVE los diccionarios
def mejor_y_peor_promedio(alumnos):
    if not alumnos:
        return None, None
    promedios = [
        {"nombre": alumno["nombre"], "promedio": sum(alumno["notas"]) / len(alumno["notas"])}
        for alumno in alumnos
    ]
    mejor = max(promedios, key=lambda x: x["promedio"])
    peor = min(promedios, key=lambda x: x["promedio"])
    return mejor, peor

# PROBLEMA 07b (buscar)
def buscar_alumno(alumnos, nombre_buscar):
    if not alumnos:
        print("No hay alumnos cargados.")
        return
    resultados = []
    for alumno in alumnos:
        if nombre_buscar.lower() in alumno["nombre"].lower():
            promedio = sum(alumno["notas"]) / len(alumno["notas"])
            resultados.append({"nombre": alumno["nombre"], "notas": alumno["notas"], "promedio": promedio})
    if resultados:
        print("\n🔎 Resultados de búsqueda:")
        for e in resultados:
            print(f"- {e['nombre']}, Notas: {e['notas']}, Promedio: {e['promedio']:.2f}")
    else:
        print(" No se encontró ningún alumno con ese nombre.")

# MENÚ PRINCIPAL
def menu():
    alumnos = []
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Cargar alumnos")
        print("2. Mostrar aprobados y desaprobados")
        print("3. Calcular promedio del curso")
        print("4. Mostrar mejor y peor promedio")
        print("5. Buscar alumno por nombre")
        print("6. Rectángulo y cuadrado (área)")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            alumnos = cargar_alumnos()
            input("\nPresiona Enter para continuar...")
        elif opcion == "2":
            contar_aprobados(alumnos)
            input("\nPresiona Enter para continuar...")
        elif opcion == "3":
            promedio_curso(alumnos)
            input("\nPresiona Enter para continuar...")
        elif opcion == "4":
            print(f"Mejor promedio: {mejor['nombre']} con {mejor['promedio']:.2f}") 
            print((f"Peor promedio: {peor['nombre']} con {peor['promedio']:.2f}"))  
            input ("\nPresiona Enter para continuar...")
        elif opcion == "5":
            nombre = input("Ingrese nombre (completo o parcial): ")
            buscar_alumno(alumnos, nombre)
            input("\nPresiona Enter para continuar...")
        elif opcion == "6":
            print("\nRectángulo")
            try:
                largo = float(input("Ingrese el largo: "))
                ancho = float(input("Ingrese el ancho: "))
                rect = Rectangulo(largo, ancho)
                print(f"Área del rectángulo: {rect.area()}")
            except ValueError:
                print("Valores inválidos para rectángulo.")

            print("\nCuadrado")
            try:
                lado = float(input("Ingrese el lado: "))
                cuad = Cuadrado(lado)
                print(f"Área del cuadrado: {cuad.area()}")
            except ValueError:
                print("Valor inválido para lado.")
                input("\nPresiona Enter para continuar...")
        elif opcion == "0":
            print(" ¡Hasta luego!")
            break
        else:
            print(" Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu()