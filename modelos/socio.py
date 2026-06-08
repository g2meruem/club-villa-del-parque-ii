from config.conexion import obtener_conexion


class Socio:

    @staticmethod
    def obtener_todos():

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            SELECT
                IdSocio,
                Nombre,
                Apellido,
                DNI,
                Telefono,
                Direccion,
                Activo
            FROM Socios
            ORDER BY Apellido, Nombre
        """)

        socios = cursor.fetchall()

        conexion.close()

        return socios

    @staticmethod
    def agregar(nombre, apellido, dni, telefono, direccion):

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO Socios
            (
                Nombre,
                Apellido,
                DNI,
                Telefono,
                Direccion
            )
            VALUES
            (?, ?, ?, ?, ?)
        """,
        (
            nombre,
            apellido,
            dni,
            telefono,
            direccion
        ))

        conexion.commit()

        conexion.close()