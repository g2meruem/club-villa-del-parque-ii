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
    from config.conexion import obtener_conexion


def listar_socios():

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            IdSocio,
            Nombre,
            Apellido,
            DNI
        FROM Socios
        WHERE Activo = 1
    """)

    socios = cursor.fetchall()

    print("\nSOCIOS REGISTRADOS\n")

    for socio in socios:

        print(
            socio.IdSocio,
            socio.Nombre,
            socio.Apellido,
            socio.DNI
        )

    conexion.close()
    from config.conexion import obtener_conexion


def eliminar_socio():

    id_socio = input("ID Socio: ")

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE Socios
        SET Activo = 0
        WHERE IdSocio = ?
    """,
    (id_socio,)
    )

    conexion.commit()

    print("Socio dado de baja.")

    conexion.close()