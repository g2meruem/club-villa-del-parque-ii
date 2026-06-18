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
                CuotaMensual
            FROM Deportes
            WHERE Activo = 1
            ORDER BY Nombre
        """)

        deportes = cursor.fetchall()

        conexion.close()

        return deportes