from config.conexion import obtener_conexion


class Invitado:

    @staticmethod
    def agregar(
        nombre,
        apellido,
        dni,
        id_deporte,
        importe
    ):

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO Invitados
            (
                Nombre,
                Apellido,
                DNI,
                IdDeporte,
                Importe
            )
            VALUES
            (?, ?, ?, ?, ?)
        """,
        (
            nombre,
            apellido,
            dni,
            id_deporte,
            importe
        ))

        conexion.commit()

        conexion.close()

    @staticmethod
    def obtener_todos():

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            SELECT
                I.IdInvitado,
                I.Nombre + ' ' + I.Apellido AS Invitado,
                I.DNI,
                D.Nombre AS Deporte,
                I.Importe,
                I.FechaVisita
            FROM Invitados I
            INNER JOIN Deportes D
                ON I.IdDeporte = D.IdDeporte
            ORDER BY I.FechaVisita DESC
        """)

        datos = cursor.fetchall()

        conexion.close()

        return datos