import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from modelos.deporte import Deporte


class VentanaDeportes:

    def __init__(self):

        self.id_seleccionado = None

        self.ventana = tk.Toplevel()

        self.ventana.title(
            "Gestión de Deportes"
        )

        self.ventana.geometry("800x500")

        self.crear_componentes()

        self.cargar_datos()

    def crear_componentes(self):

        frame = tk.Frame(self.ventana)

        frame.pack(pady=10)

        tk.Label(
            frame,
            text="Nombre"
        ).grid(
            row=0,
            column=0
        )

        self.txt_nombre = tk.Entry(
            frame
        )

        self.txt_nombre.grid(
            row=0,
            column=1
        )

        tk.Label(
            frame,
            text="Cuota"
        ).grid(
            row=0,
            column=2
        )

        self.txt_cuota = tk.Entry(
            frame
        )

        self.txt_cuota.grid(
            row=0,
            column=3
        )

        tk.Button(
            frame,
            text="Agregar",
            command=self.guardar
        ).grid(
            row=1,
            column=0,
            pady=10
        )

        tk.Button(
            frame,
            text="Modificar",
            command=self.modificar
        ).grid(
            row=1,
            column=1
        )

        tk.Button(
            frame,
            text="Eliminar",
            command=self.eliminar
        ).grid(
            row=1,
            column=2
        )

        tk.Button(
            frame,
            text="Refrescar",
            command=self.cargar_datos
        ).grid(
            row=1,
            column=3
        )

        self.tabla = ttk.Treeview(
            self.ventana,
            columns=(
                "ID",
                "Nombre",
                "Cuota",
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
            "Cuota",
            text="Cuota"
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

        self.tabla.bind(
            "<<TreeviewSelect>>",
            self.seleccionar_deporte
        )

    def cargar_datos(self):

        for fila in self.tabla.get_children():

            self.tabla.delete(fila)

        deportes = Deporte.obtener_todos()

        for deporte in deportes:

            self.tabla.insert(
                "",
                tk.END,
                values=(
                    deporte.IdDeporte,
                    deporte.Nombre,
                    deporte.CuotaMensual,
                    deporte.Activo
                )
            )

    def guardar(self):

        Deporte.agregar(
            self.txt_nombre.get(),
            self.txt_cuota.get()
        )

        self.cargar_datos()

        self.limpiar()

        messagebox.showinfo(
            "Correcto",
            "Deporte agregado"
        )

    def seleccionar_deporte(self, event):

        seleccion = self.tabla.selection()

        if not seleccion:
            return

        valores = self.tabla.item(
            seleccion[0]
        )["values"]

        self.id_seleccionado = valores[0]

        self.txt_nombre.delete(
            0,
            tk.END
        )

        self.txt_nombre.insert(
            0,
            valores[1]
        )

        self.txt_cuota.delete(
            0,
            tk.END
        )

        self.txt_cuota.insert(
            0,
            valores[2]
        )

    def modificar(self):

        if self.id_seleccionado is None:

            messagebox.showwarning(
                "Aviso",
                "Seleccione un deporte"
            )

            return

        Deporte.actualizar(
            self.id_seleccionado,
            self.txt_nombre.get(),
            self.txt_cuota.get()
        )

        self.cargar_datos()

        self.limpiar()

        messagebox.showinfo(
            "Correcto",
            "Deporte actualizado"
        )

    def eliminar(self):

        if self.id_seleccionado is None:

            messagebox.showwarning(
                "Aviso",
                "Seleccione un deporte"
            )

            return

        respuesta = messagebox.askyesno(
            "Confirmar",
            "¿Desea desactivar este deporte?"
        )

        if respuesta:

            Deporte.baja_logica(
                self.id_seleccionado
            )

            self.cargar_datos()

            self.limpiar()

            messagebox.showinfo(
                "Correcto",
                "Deporte desactivado"
            )

    def limpiar(self):

        self.txt_nombre.delete(
            0,
            tk.END
        )

        self.txt_cuota.delete(
            0,
            tk.END
        )

        self.id_seleccionado = None