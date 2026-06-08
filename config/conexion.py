import pyodbc


def obtener_conexion():
    try:
        conexion = pyodbc.connect(
            "DRIVER={SQL Server};"
            "SERVER=localhost\\SQLEXPRESS;"
            "DATABASE=ClubVillaDelParqueII;"
            "Trusted_Connection=yes;"
        )

        return conexion

    except Exception as e:
        print("Error de conexión:")
        print(e)
        return None