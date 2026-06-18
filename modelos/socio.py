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
    @staticmethod
    def actualizar(id_socio, nombre, apellido, dni, telefono, direccion):

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
        UPDATE Socios
        SET
            Nombre = ?,
            Apellido = ?,
            DNI = ?,
            Telefono = ?,
            Direccion = ?
        WHERE IdSocio = ?
        """,
        (
        nombre,
        apellido,
        dni,
        telefono,
        direccion,
        id_socio
        ))

        conexion.commit()

        conexion.close()


    @staticmethod
    def baja_logica(id_socio):

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE Socios
            SET Activo = 0
            WHERE IdSocio = ?
        """, (id_socio,))

        print("Filas afectadas:", cursor.rowcount)

        conexion.commit()

        conexion.close()

    @staticmethod
    def buscar_por_dni(dni):

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
        WHERE DNI LIKE ?
        """,
        (f"%{dni}%",))

        resultado = cursor.fetchall()

        conexion.close()

        return resultado  
    @staticmethod
    def obtener_activos():

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            SELECT
                IdSocio,
                Nombre,
                Apellido
            FROM Socios
            WHERE Activo = 1
            ORDER BY Apellido
        """)

        resultado = cursor.fetchall()

        conexion.close()

        return resultado