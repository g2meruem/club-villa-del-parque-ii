from config.conexion import obtener_conexion


def agregar_socio():

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    telefono = input("Telefono: ")
    direccion = input("Direccion: ")

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO Socios
        (
            Nombre,
            Apellido,
            DNI,
            Telefono,
            Direccion,
            TipoPersona
        )
        VALUES
        (?, ?, ?, ?, ?, 'Socio')
    """,
    (
        nombre,
        apellido,
        dni,
        telefono,
        direccion
    ))

    conexion.commit()

    print("Socio agregado correctamente.")

    conexion.close()