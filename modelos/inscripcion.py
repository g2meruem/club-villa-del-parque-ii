from config.conexion import obtener_conexion


class Inscripcion:

    @staticmethod
    def agregar(id_socio, id_deporte):

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO Inscripciones
            (
                IdSocio,
                IdDeporte
            )
            VALUES
            (?, ?)
        """,
        (
            id_socio,
            id_deporte
        ))

        conexion.commit()

        conexion.close()

    @staticmethod
    def obtener_todas():

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            SELECT
                I.IdInscripcion,
                S.Nombre + ' ' + S.Apellido AS Socio,
                D.Nombre AS Deporte,
                I.FechaInscripcion
            FROM Inscripciones I
            INNER JOIN Socios S
                ON I.IdSocio = S.IdSocio
            INNER JOIN Deportes D
                ON I.IdDeporte = D.IdDeporte
            WHERE I.Activo = 1
            ORDER BY S.Apellido
        """)

        resultado = cursor.fetchall()

        conexion.close()

        return resultado