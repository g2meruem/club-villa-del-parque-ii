import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from modelos.socio import Socio


class VentanaSocios:

    def __init__(self):

        self.id_seleccionado = None

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

        # Nombre

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

        # Apellido

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

        # DNI

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

        # Teléfono

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

        # Dirección

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

        # Botones

        tk.Button(
            frame_formulario,
            text="Guardar Socio",
            command=self.guardar
        ).grid(
            row=3,
            column=0,
            pady=10
        )

        tk.Button(
            frame_formulario,
            text="Modificar",
            command=self.modificar
        ).grid(
            row=3,
            column=1,
            pady=10
        )

        tk.Button(
            frame_formulario,
            text="Eliminar",
            command=self.eliminar
        ).grid(
            row=3,
            column=2,
            pady=10
        )

        tk.Button(
            frame_formulario,
            text="Refrescar",
            command=self.cargar_socios
        ).grid(
            row=3,
            column=3,
            pady=10
        )

        # Tabla

        self.tabla = ttk.Treeview(
            self.ventana,
            columns=(
                "ID",
                "Nombre",
                "Apellido",
                "DNI",
                "Telefono",
                "Direccion",
                "Activo"
            ),
            show="headings"
        )

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Apellido", text="Apellido")
        self.tabla.heading("DNI", text="DNI")
        self.tabla.heading("Telefono", text="Teléfono")
        self.tabla.heading("Direccion", text="Dirección")
        self.tabla.heading("Activo", text="Activo")

        self.tabla.column("ID", width=60)
        self.tabla.column("Nombre", width=120)
        self.tabla.column("Apellido", width=120)
        self.tabla.column("DNI", width=100)
        self.tabla.column("Telefono", width=120)
        self.tabla.column("Direccion", width=200)
        self.tabla.column("Activo", width=80)

        self.tabla.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.tabla.bind(
            "<<TreeviewSelect>>",
            self.seleccionar_socio
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
                    socio.Direccion,
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

    def seleccionar_socio(self, event):

        seleccion = self.tabla.selection()

        if not seleccion:
            return

        valores = self.tabla.item(
            seleccion[0]
        )["values"]

        self.id_seleccionado = valores[0]

        self.txt_nombre.delete(0, tk.END)
        self.txt_nombre.insert(0, valores[1])

        self.txt_apellido.delete(0, tk.END)
        self.txt_apellido.insert(0, valores[2])

        self.txt_dni.delete(0, tk.END)
        self.txt_dni.insert(0, valores[3])

        self.txt_telefono.delete(0, tk.END)
        self.txt_telefono.insert(0, valores[4])

        self.txt_direccion.delete(0, tk.END)
        self.txt_direccion.insert(0, valores[5])

    def modificar(self):

        if self.id_seleccionado is None:

            messagebox.showwarning(
                "Aviso",
                "Seleccione un socio"
            )

            return

        Socio.actualizar(
            self.id_seleccionado,
            self.txt_nombre.get(),
            self.txt_apellido.get(),
            self.txt_dni.get(),
            self.txt_telefono.get(),
            self.txt_direccion.get()
        )

        self.cargar_socios()

        self.limpiar()

        self.id_seleccionado = None

        messagebox.showinfo(
            "Correcto",
            "Socio actualizado"
        )

    def eliminar(self):

        if self.id_seleccionado is None:

            messagebox.showwarning(
                "Aviso",
                "Seleccione un socio"
            )

            return

        respuesta = messagebox.askyesno(
            "Confirmar",
            "¿Desea dar de baja este socio?"
        )

        if respuesta:
            print("ID seleccionado:", self.id_seleccionado)
            Socio.baja_logica(
                self.id_seleccionado
            )

            self.cargar_socios()

            self.limpiar()

            self.id_seleccionado = None

            messagebox.showinfo(
                "Correcto",
                "Socio dado de baja"
            )

    def limpiar(self):

        self.txt_nombre.delete(0, tk.END)
        self.txt_apellido.delete(0, tk.END)
        self.txt_dni.delete(0, tk.END)
        self.txt_telefono.delete(0, tk.END)
        self.txt_direccion.delete(0, tk.END)