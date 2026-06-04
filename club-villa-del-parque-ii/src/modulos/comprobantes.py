from datetime import datetime


def emitir_comprobante(
        nombre,
        concepto,
        importe):

    print()

    print("=" * 40)

    print("CLUB VILLA DEL PARQUE II")

    print("=" * 40)

    print("Fecha:",
          datetime.now())

    print()

    print("Socio:", nombre)

    print("Concepto:", concepto)

    print("Importe: $", importe)

    print()

    print("PAGO REGISTRADO")

    print("=" * 40)