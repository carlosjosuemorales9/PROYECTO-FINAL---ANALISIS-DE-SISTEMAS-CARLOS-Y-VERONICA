# SISTEMA ESCOLAR EN TERMINAL - SIN ARCHIVOS
alumnos = {}
docentes = {}
materias = {}
grupos = {}
calificaciones = {}

# -------------------- GESTIÓN DE ALUMNOS --------------------
def menu_alumnos():
    while True:
        print("\n--- GESTIÓN DE ALUMNOS ---")
        print("1. Agregar Alumno")
        print("2. Buscar Alumno")
        print("3. Modificar Alumno")
        print("4. Eliminar Alumno")
        print("5. Volver")
        op = input("Seleccione una opción: ")
        if op == "1":
            agregar_alumno()
        elif op == "2":
            buscar_alumno()
        elif op == "3":
            modificar_alumno()
        elif op == "4":
            eliminar_alumno()
        elif op == "5":
            break

def agregar_alumno():
    control = input("Número de control: ")
    if control in alumnos:
        print("Ya existe ese número de control.")
        return
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ")
    alumnos[control] = {
        "nombre": nombre,
        "apellidos": apellidos,
        "direccion": direccion,
        "telefono": telefono,
        "nacimiento": nacimiento
    }
    print("Alumno agregado con éxito.")

def buscar_alumno():
    control = input("Ingrese número de control: ")
    if control in alumnos:
        print(alumnos[control])
    else:
        print("Alumno no encontrado.")

def modificar_alumno():
    control = input("Número de control del alumno: ")
    if control in alumnos:
        print("Ingrese nuevos datos:")
        alumnos[control]["nombre"] = input("Nombre: ")
        alumnos[control]["apellidos"] = input("Apellidos: ")
        alumnos[control]["direccion"] = input("Dirección: ")
        alumnos[control]["telefono"] = input("Teléfono: ")
        alumnos[control]["nacimiento"] = input("Fecha de nacimiento: ")
        print("Alumno modificado.")
    else:
        print("Alumno no encontrado.")

def eliminar_alumno():
    control = input("Número de control a eliminar: ")
    if alumnos.pop(control, None):
        print("Alumno eliminado.")
    else:
        print("Alumno no encontrado.")

# -------------------- GESTIÓN DE DOCENTES --------------------
def menu_docentes():
    while True:
        print("\n--- GESTIÓN DE DOCENTES ---")
        print("1. Agregar Docente")
        print("2. Buscar Docente")
        print("3. Modificar Docente")
        print("4. Eliminar Docente")
        print("5. Volver")
        op = input("Seleccione una opción: ")
        if op == "1":
            agregar_docente()
        elif op == "2":
            buscar_docente()
        elif op == "3":
            modificar_docente()
        elif op == "4":
            eliminar_docente()
        elif op == "5":
            break

def agregar_docente():
    emp = input("Número de empleado: ")
    if emp in docentes:
        print("Ya existe ese número.")
        return
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    categoria = input("Categoría: ")
    horas = input("Horas trabajadas: ")
    horario = input("Horario: ")
    docentes[emp] = {
        "nombre": nombre,
        "apellidos": apellidos,
        "categoria": categoria,
        "horas": horas,
        "horario": horario
    }
    print("Docente agregado.")

def buscar_docente():
    emp = input("Número de empleado: ")
    if emp in docentes:
        print(docentes[emp])
    else:
        print("Docente no encontrado.")

def modificar_docente():
    emp = input("Número de empleado: ")
    if emp in docentes:
        docentes[emp]["nombre"] = input("Nombre: ")
        docentes[emp]["apellidos"] = input("Apellidos: ")
        docentes[emp]["categoria"] = input("Categoría: ")
        docentes[emp]["horas"] = input("Horas trabajadas: ")
        docentes[emp]["horario"] = input("Horario: ")
        print("Docente modificado.")
    else:
        print("Docente no encontrado.")

def eliminar_docente():
    emp = input("Número de empleado a eliminar: ")
    if docentes.pop(emp, None):
        print("Docente eliminado.")
    else:
        print("Docente no encontrado.")

# -------------------- GESTIÓN DE MATERIAS --------------------
def menu_materias():
    while True:
        print("\n--- GESTIÓN DE MATERIAS ---")
        print("1. Agregar Materia")
        print("2. Buscar Materia")
        print("3. Modificar Materia")
        print("4. Eliminar Materia")
        print("5. Volver")
        op = input("Seleccione una opción: ")
        if op == "1":
            agregar_materia()
        elif op == "2":
            buscar_materia()
        elif op == "3":
            modificar_materia()
        elif op == "4":
            eliminar_materia()
        elif op == "5":
            break

def agregar_materia():
    clave = input("Clave de materia: ")
    if clave in materias:
        print("Ya existe esa clave.")
        return
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    plan = input("Plan de estudios: ")
    materias[clave] = {
        "nombre": nombre,
        "descripcion": descripcion,
        "plan": plan
    }
    print("Materia registrada.")

def buscar_materia():
    clave = input("Clave de materia: ")
    if clave in materias:
        print(materias[clave])
    else:
        print("Materia no encontrada.")

def modificar_materia():
    clave = input("Clave de materia: ")
    if clave in materias:
        materias[clave]["nombre"] = input("Nombre: ")
        materias[clave]["descripcion"] = input("Descripción: ")
        materias[clave]["plan"] = input("Plan de estudios: ")
        print("Materia modificada.")
    else:
        print("Materia no encontrada.")

def eliminar_materia():
    clave = input("Clave de materia a eliminar: ")
    if materias.pop(clave, None):
        print("Materia eliminada.")
    else:
        print("No existe esa materia.")

# -------------------- GRUPOS --------------------
def agregar_grupo():
    clave = input("Clave de grupo: ")
    docente = input("Docente (número): ")
    materia = input("Clave materia: ")
    horario = input("Horario: ")
    grupos[clave] = {
        "docente": docente,
        "materia": materia,
        "horario": horario
    }
    print("Grupo agregado.")

# -------------------- LISTADO DE ALUMNOS --------------------
def listado_alumnos():
    print("\n--- LISTADO DE ALUMNOS ---")
    for control, datos in alumnos.items():
        grupo = input(f"Clave grupo para {datos['nombre']}: ")
        materia = input(f"Clave materia para {datos['nombre']}: ")
        print(f"{control} | {datos['nombre']} {datos['apellidos']} | Grupo: {grupo} | Materia: {materia}")

# -------------------- CALIFICACIONES --------------------
def calificar_alumnos():
    grupo = input("Clave grupo: ")
    materia = input("Materia: ")
    horario = input("Horario: ")
    for control, datos in alumnos.items():
        calif = input(f"Calificación de {datos['nombre']} {datos['apellidos']}: ")
        calificaciones[control] = {
            "grupo": grupo,
            "materia": materia,
            "horario": horario,
            "calificacion": calif
        }
    print("Calificaciones registradas.")

# -------------------- MENÚ PRINCIPAL --------------------
def menu():
    while True:
        print("\n====== SISTEMA ESCOLAR EN TERMINAL ======")
        print("1. Gestión de Alumnos")
        print("2. Gestión de Docentes")
        print("3. Gestión de Materias")
        print("4. Agregar Grupos")
        print("5. Listado de Alumnos")
        print("6. Calificar Alumnos")
        print("7. Salir")
        opc = input("Seleccione una opción: ")
        if opc == "1":
            menu_alumnos()
        elif opc == "2":
            menu_docentes()
        elif opc == "3":
            menu_materias()
        elif opc == "4":
            agregar_grupo()
        elif opc == "5":
            listado_alumnos()
        elif opc == "6":
            calificar_alumnos()
        elif opc == "7":
            print("¡Hasta pronto")
            break
        else:
            print("Opción inválida.")

# Ejecutar el programa
menu()
