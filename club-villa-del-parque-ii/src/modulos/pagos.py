from config.conexion import obtener_conexion


def registrar_pago():

    id_socio = input("ID Socio: ")

    concepto = input("Concepto: ")

    importe = float(input("Importe: "))

    medio_pago = input("Medio de Pago: ")

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    cursor.execute("""
        EXEC sp_RegistrarPago
        ?, ?, ?, ?
    """,
    (
        id_socio,
        concepto,
        importe,
        medio_pago
    ))

    conexion.commit()

    print("Pago registrado.")

    conexion.close()