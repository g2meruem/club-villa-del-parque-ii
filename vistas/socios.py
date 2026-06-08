import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from modelos.socio import Socio


class VentanaSocios:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title(
            "Gestión de Socios"
        )

        self.ventana.geometry("900x500")

        self.crear_componentes()

        self.cargar_socios()

    def crear_componentes(self):

        frame_formulario = tk.Frame(
            self.ventana
        )

        frame_formulario.pack(
            pady=10
        )

        tk.Label(
            frame_formulario,
            text="Nombre"
        ).grid(
            row=0,
            column=0
        )

        self.txt_nombre = tk.Entry(
            frame_formulario
        )

        self.txt_nombre.grid(
            row=0,
            column=1
        )

        tk.Label(
            frame_formulario,
            text="Apellido"
        ).grid(
            row=0,
            column=2
        )

        self.txt_apellido = tk.Entry(
            frame_formulario
        )

        self.txt_apellido.grid(
            row=0,
            column=3
        )

        tk.Label(
            frame_formulario,
            text="DNI"
        ).grid(
            row=1,
            column=0
        )

        self.txt_dni = tk.Entry(
            frame_formulario
        )

        self.txt_dni.grid(
            row=1,
            column=1
        )

        tk.Label(
            frame_formulario,
            text="Teléfono"
        ).grid(
            row=1,
            column=2
        )

        self.txt_telefono = tk.Entry(
            frame_formulario
        )

        self.txt_telefono.grid(
            row=1,
            column=3
        )

        tk.Label(
            frame_formulario,
            text="Dirección"
        ).grid(
            row=2,
            column=0
        )

        self.txt_direccion = tk.Entry(
            frame_formulario,
            width=40
        )

        self.txt_direccion.grid(
            row=2,
            column=1,
            columnspan=3
        )

        tk.Button(
            frame_formulario,
            text="Guardar Socio",
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
                "Nombre",
                "Apellido",
                "DNI",
                "Telefono",
                "Activo"
            ),
            show="headings"
        )

        self.tabla.heading(
            "ID",
            text="ID"
        )

        self.tabla.heading(
            "Nombre",
            text="Nombre"
        )

        self.tabla.heading(
            "Apellido",
            text="Apellido"
        )

        self.tabla.heading(
            "DNI",
            text="DNI"
        )

        self.tabla.heading(
            "Telefono",
            text="Teléfono"
        )

        self.tabla.heading(
            "Activo",
            text="Activo"
        )

        self.tabla.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    def cargar_socios(self):

        for fila in self.tabla.get_children():

            self.tabla.delete(fila)

        socios = Socio.obtener_todos()

        for socio in socios:

            self.tabla.insert(
                "",
                tk.END,
                values=(
                    socio.IdSocio,
                    socio.Nombre,
                    socio.Apellido,
                    socio.DNI,
                    socio.Telefono,
                    socio.Activo
                )
            )

    def guardar(self):

        Socio.agregar(
            self.txt_nombre.get(),
            self.txt_apellido.get(),
            self.txt_dni.get(),
            self.txt_telefono.get(),
            self.txt_direccion.get()
        )

        messagebox.showinfo(
            "Correcto",
            "Socio agregado"
        )

        self.limpiar()

        self.cargar_socios()

    def limpiar(self):

        self.txt_nombre.delete(0, tk.END)

        self.txt_apellido.delete(0, tk.END)

        self.txt_dni.delete(0, tk.END)

        self.txt_telefono.delete(0, tk.END)

        self.txt_direccion.delete(0, tk.END)