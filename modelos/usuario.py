from config.conexion import obtener_conexion


class Usuario:

    @staticmethod
    def validar(usuario, password):

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""
            SELECT
                u.IdUsuario,
                u.Usuario,
                r.NombreRol
            FROM Usuarios u
            INNER JOIN Roles r
                ON u.IdRol = r.IdRol
            WHERE u.Usuario = ?
            AND u.PasswordHash = ?
        """,
        (usuario, password))

        resultado = cursor.fetchone()

        conexion.close()

        return resultado