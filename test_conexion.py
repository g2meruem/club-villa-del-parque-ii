from config.conexion import obtener_conexion


def main():

    conexion = obtener_conexion()

    if conexion:

        print("=" * 50)
        print("CLUB VILLA DEL PARQUE II")
        print("=" * 50)

        print("Conexión a SQL Server exitosa")

        cursor = conexion.cursor()

        cursor.execute("""
            SELECT DB_NAME()
        """)

        resultado = cursor.fetchone()

        print("Base de datos:", resultado[0])

        conexion.close()

    else:

        print("No se pudo conectar.")


if __name__ == "__main__":
    main()