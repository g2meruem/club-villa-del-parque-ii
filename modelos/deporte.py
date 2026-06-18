from config.conexion import obtener_conexion


class Deporte:

    @staticmethod
    def obtener_todos():

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            SELECT
                IdDeporte,
                Nombre,
                CuotaMensual,
                Activo
            FROM Deportes
            ORDER BY Nombre
        """)

        deportes = cursor.fetchall()

        conexion.close()

        return deportes

    @staticmethod
    def obtener_combo():

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            SELECT
                IdDeporte,
                Nombre
            FROM Deportes
            WHERE Activo = 1
            ORDER BY Nombre
        """)

        resultado = cursor.fetchall()

        conexion.close()

        return resultado

    @staticmethod
    def agregar(nombre, cuota):

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO Deportes
            (
                Nombre,
                CuotaMensual
            )
            VALUES
            (?, ?)
        """,
        (
            nombre,
            cuota
        ))

        conexion.commit()

        conexion.close()

    @staticmethod
    def actualizar(
        id_deporte,
        nombre,
        cuota
    ):

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE Deportes
            SET
                Nombre = ?,
                CuotaMensual = ?
            WHERE IdDeporte = ?
        """,
        (
            nombre,
            cuota,
            id_deporte
        ))

        conexion.commit()

        conexion.close()

    @staticmethod
    def baja_logica(id_deporte):

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE Deportes
            SET Activo = 0
            WHERE IdDeporte = ?
        """,
        (
            id_deporte,
        ))

        conexion.commit()

        conexion.close()