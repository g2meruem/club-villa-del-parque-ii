from modulos.socios import (
    agregar_socio,
    listar_socios,
    eliminar_socio
)


def menu_socios():

    while True:

        print("\n--- SOCIOS ---")

        print("1. Agregar")

        print("2. Listar")

        print("3. Eliminar")

        print("0. Volver")

        opcion = input("Opcion: ")

        if opcion == "1":
            agregar_socio()

        elif opcion == "2":
            listar_socios()

        elif opcion == "3":
            eliminar_socio()

        elif opcion == "0":
            break