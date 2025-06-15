def mostrar_menu():
    print("\n===== Sistema de Registro de Estudiantes =====")
    print("1. Registrar nuevo estudiante")
    print("2. Ver lista de estudiantes")
    print("3. Salir")

def registrar_estudiante():
    print("\n--- Registro de Estudiante ---")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    grado = input("Grado: ")

    with open("estudiantes.txt", "a") as archivo:
        archivo.write(f"{nombre},{apellido},{edad},{grado}\n")

    print("✅ Estudiante registrado correctamente.")

def ver_estudiantes():
    print("\n--- Lista de Estudiantes Registrados ---")
    try:
        with open("estudiantes.txt", "r") as archivo:
            estudiantes = archivo.readlines()
            if not estudiantes:
                print("⚠️ No hay estudiantes registrados.")
            else:
                for i, est in enumerate(estudiantes, 1):
                    nombre, apellido, edad, grado = est.strip().split(",")
                    print(f"{i}. {nombre} {apellido}, Edad: {edad}, Grado: {grado}")
    except FileNotFoundError:
        print("⚠️ El archivo de estudiantes no existe aún.")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-3): ")

    if opcion == "1":
        registrar_estudiante()
    elif opcion == "2":
        ver_estudiantes()
    elif opcion == "3":
        print("👋 Saliendo del sistema. ¡Hasta pronto!")
        break
    else:
        print("❌ Opción no válida. Intente de nuevo.")
