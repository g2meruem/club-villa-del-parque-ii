from menus.menu_socios import menu_socios


def menu_principal():

    while True:

        print()

        print("=" * 50)

        print("CLUB VILLA DEL PARQUE II")

        print("=" * 50)

        print("1. Gestion de Socios")

        print("2. Gestion de Pagos")

        print("3. Rendicion Mensual")

        print("0. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":

            menu_socios()

        elif opcion == "0":

            print("Fin del programa")

            break