import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from modelos.invitado import Invitado
from modelos.deporte import Deporte


class VentanaInvitados:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title(
            "Gestión de Invitados"
        )

        self.ventana.geometry(
            "900x500"
        )

        self.crear_componentes()

        self.cargar_deportes()

        self.cargar_tabla()

    def crear_componentes(self):

        frame = tk.Frame(self.ventana)

        frame.pack(pady=10)

        tk.Label(frame, text="Nombre").grid(row=0, column=0)
        self.txt_nombre = tk.Entry(frame)
        self.txt_nombre.grid(row=0, column=1)

        tk.Label(frame, text="Apellido").grid(row=0, column=2)
        self.txt_apellido = tk.Entry(frame)
        self.txt_apellido.grid(row=0, column=3)

        tk.Label(frame, text="DNI").grid(row=1, column=0)
        self.txt_dni = tk.Entry(frame)
        self.txt_dni.grid(row=1, column=1)

        tk.Label(frame, text="Importe").grid(row=1, column=2)
        self.txt_importe = tk.Entry(frame)
        self.txt_importe.grid(row=1, column=3)

        tk.Label(frame, text="Deporte").grid(row=2, column=0)

        self.cbo_deporte = ttk.Combobox(
            frame,
            state="readonly"
        )

        self.cbo_deporte.grid(
            row=2,
            column=1
        )

        tk.Button(
            frame,
            text="Registrar Invitado",
            command=self.guardar
        ).grid(
            row=3,
            column=0,
            columnspan=4,
            pady=10
        )

        self.tabla = ttk.Treeview(
            self.ventana,
            columns=(
                "ID",
                "Invitado",
                "DNI",
                "Deporte",
                "Importe",
                "Fecha"
            ),
            show="headings"
        )

        for columna in (
            "ID",
            "Invitado",
            "DNI",
            "Deporte",
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

    def cargar_deportes(self):

        self.deportes = Deporte.obtener_combo()

        self.cbo_deporte["values"] = [
            f"{d.IdDeporte} - {d.Nombre}"
            for d in self.deportes
        ]

    def cargar_tabla(self):

        for fila in self.tabla.get_children():

            self.tabla.delete(fila)

        invitados = Invitado.obtener_todos()

        for invitado in invitados:

            self.tabla.insert(
                "",
                tk.END,
                values=(
                    invitado.IdInvitado,
                    invitado.Invitado,
                    invitado.DNI,
                    invitado.Deporte,
                    invitado.Importe,
                    invitado.FechaVisita
                )
            )

    def guardar(self):

        id_deporte = int(
            self.cbo_deporte.get().split("-")[0]
        )

        Invitado.agregar(
            self.txt_nombre.get(),
            self.txt_apellido.get(),
            self.txt_dni.get(),
            id_deporte,
            self.txt_importe.get()
        )

        self.cargar_tabla()

        messagebox.showinfo(
            "Correcto",
            "Invitado registrado"
        )