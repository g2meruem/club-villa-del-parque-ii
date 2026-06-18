from config.conexion import obtener_conexion


class Reporte:

    @staticmethod
    def cantidad_socios():

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM Socios
            WHERE Activo = 1
        """)

        resultado = cursor.fetchone()[0]

        conexion.close()

        return resultado

    @staticmethod
    def cantidad_inscripciones():

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM Inscripciones
            WHERE Activo = 1
        """)

        resultado = cursor.fetchone()[0]

        conexion.close()

        return resultado

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
    def total_invitados():

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            SELECT ISNULL(
                SUM(Importe),
                0
            )
            FROM Invitados
        """)

        total = cursor.fetchone()[0]

        conexion.close()

        return total

    @staticmethod
    def socios_por_deporte():

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            SELECT
                D.Nombre,
                COUNT(*) AS Cantidad
            FROM Inscripciones I
            INNER JOIN Deportes D
                ON I.IdDeporte = D.IdDeporte
            WHERE I.Activo = 1
            GROUP BY D.Nombre
            ORDER BY Cantidad DESC
        """)

        datos = cursor.fetchall()

        conexion.close()

        return datos

    @staticmethod
    def deporte_mas_popular():

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            SELECT TOP 1
                D.Nombre,
                COUNT(*) AS Cantidad
            FROM Inscripciones I
            INNER JOIN Deportes D
                ON I.IdDeporte = D.IdDeporte
            WHERE I.Activo = 1
            GROUP BY D.Nombre
            ORDER BY Cantidad DESC
        """)

        resultado = cursor.fetchone()

        conexion.close()

        return resultado

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
            ORDER BY Concepto
        """)

        datos = cursor.fetchall()

        conexion.close()

        return datos

    @staticmethod
    def pagos_mes_actual():

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM Pagos
            WHERE
                MONTH(FechaPago) = MONTH(GETDATE())
            AND
                YEAR(FechaPago) = YEAR(GETDATE())
        """)

        resultado = cursor.fetchone()[0]

        conexion.close()

        return resultado

    @staticmethod
    def ultimos_pagos():

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            SELECT TOP 10
                IdPago,
                Concepto,
                Importe,
                FechaPago
            FROM Pagos
            ORDER BY FechaPago DESC
        """)

        datos = cursor.fetchall()

        conexion.close()

        return datos

    @staticmethod
    def invitados_por_deporte():

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            SELECT
                D.Nombre,
                COUNT(*) AS Cantidad
            FROM Invitados I
            INNER JOIN Deportes D
                ON I.IdDeporte = D.IdDeporte
            GROUP BY D.Nombre
            ORDER BY Cantidad DESC
        """)

        datos = cursor.fetchall()

        conexion.close()

        return datos

    @staticmethod
    def cantidad_invitados():

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM Invitados
        """)

        resultado = cursor.fetchone()[0]

        conexion.close()

        return resultado