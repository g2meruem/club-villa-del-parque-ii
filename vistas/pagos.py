import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from modelos.socio import Socio
from modelos.pago import Pago


class VentanaPagos:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title(
            "Registro de Pagos"
        )

        self.ventana.geometry("900x500")

        self.crear_componentes()

        self.cargar_socios()

        self.cargar_tabla()

    def crear_componentes(self):

        frame = tk.Frame(self.ventana)

        frame.pack(pady=10)

        tk.Label(
            frame,
            text="Socio"
        ).grid(row=0, column=0)

        self.cbo_socio = ttk.Combobox(
            frame,
            width=40,
            state="readonly"
        )

        self.cbo_socio.grid(
            row=0,
            column=1
        )

        tk.Label(
            frame,
            text="Concepto"
        ).grid(row=1, column=0)

        self.cbo_concepto = ttk.Combobox(
            frame,
            values=[
                "Cuota Social",
                "Cuota Deportiva"
            ],
            state="readonly"
        )

        self.cbo_concepto.grid(
            row=1,
            column=1
        )

        tk.Label(
            frame,
            text="Importe"
        ).grid(row=2, column=0)

        self.txt_importe = tk.Entry(
            frame
        )

        self.txt_importe.grid(
            row=2,
            column=1
        )

        tk.Button(
            frame,
            text="Registrar Pago",
            command=self.guardar
        ).grid(
            row=3,
            column=0,
            columnspan=2,
            pady=10
        )

        self.tabla = ttk.Treeview(
            self.ventana,
            columns=(
                "ID",
                "Socio",
                "Concepto",
                "Importe",
                "Fecha"
            ),
            show="headings"
        )

        for columna in (
            "ID",
            "Socio",
            "Concepto",
            "Importe",
            "Fecha"
        ):
            self.tabla.heading(
                columna,
                text=columna
            )

        self.tabla.pack(
            fill="both",
            expand=True
        )

    def cargar_socios(self):

        socios = Socio.obtener_activos()

        self.cbo_socio["values"] = [
            f"{s.IdSocio} - {s.Apellido}, {s.Nombre}"
            for s in socios
        ]

    def cargar_tabla(self):

        for fila in self.tabla.get_children():

            self.tabla.delete(fila)

        pagos = Pago.obtener_todos()

        for pago in pagos:

            self.tabla.insert(
                "",
                tk.END,
                values=(
                    pago.IdPago,
                    pago.Socio,
                    pago.Concepto,
                    pago.Importe,
                    pago.FechaPago
                )
            )

    def guardar(self):

        if not self.cbo_socio.get():

            return

        id_socio = int(
            self.cbo_socio.get().split("-")[0]
        )

        Pago.registrar(
            id_socio,
            self.cbo_concepto.get(),
            self.txt_importe.get()
        )

        self.cargar_tabla()

        messagebox.showinfo(
            "Comprobante de Pago",
            f"""
        CLUB VILLA DEL PARQUE II

        Socio:
        {self.cbo_socio.get()}

        Concepto:
        {self.cbo_concepto.get()}

        Importe:
        ${self.txt_importe.get()}

        Estado:
        PAGO REGISTRADO
        """
        )