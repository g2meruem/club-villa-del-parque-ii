from config.conexion import obtener_conexion


class Pago:

    @staticmethod
    def registrar(id_socio, concepto, importe):

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO Pagos
            (
                IdSocio,
                Concepto,
                Importe
            )
            VALUES
            (?, ?, ?)
        """,
        (
            id_socio,
            concepto,
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
                P.IdPago,
                S.Nombre + ' ' + S.Apellido AS Socio,
                P.Concepto,
                P.Importe,
                P.FechaPago
            FROM Pagos P
            INNER JOIN Socios S
                ON P.IdSocio = S.IdSocio
            ORDER BY P.FechaPago DESC
        """)

        datos = cursor.fetchall()

        conexion.close()

        return datos
    @staticmethod
    def total_recaudado():

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            SELECT ISNULL(
                SUM(Importe),
                0
            )
            FROM Pagos
        """)

        total = cursor.fetchone()[0]

        conexion.close()

        return total
    @staticmethod
    def recaudacion_por_concepto():

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            SELECT
                Concepto,
                SUM(Importe) AS Total
            FROM Pagos
            GROUP BY Concepto
        """)

        datos = cursor.fetchall()

        conexion.close()

        return datos
    @staticmethod
    def pagos_mes_actual():

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            SELECT
                COUNT(*)
            FROM Pagos
            WHERE
                MONTH(FechaPago)=MONTH(GETDATE())
            AND
                YEAR(FechaPago)=YEAR(GETDATE())
        """)

        cantidad = cursor.fetchone()[0]

        conexion.close()

        return cantidad