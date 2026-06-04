import pyodbc


def obtener_conexion():

    conexion = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=localhost;"
        "DATABASE=ClubVillaDelParqueII;"
        "Trusted_Connection=yes;"
    )

    return conexion