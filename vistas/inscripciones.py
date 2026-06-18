import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from modelos.socio import Socio
from modelos.deporte import Deporte
from modelos.inscripcion import Inscripcion


class VentanaInscripciones:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title(
            "Inscripciones Deportivas"
        )

        self.ventana.geometry("800x500")

        self.socios = []
        self.deportes = []

        self.crear_componentes()

        self.cargar_datos()

    def crear_componentes(self):

        frame = tk.Frame(self.ventana)
        frame.pack(pady=10)

        tk.Label(
            frame,
            text="Socio"
        ).grid(row=0, column=0)

        self.cbo_socios = ttk.Combobox(
            frame,
            width=40,
            state="readonly"
        )

        self.cbo_socios.grid(
            row=0,
            column=1,
            padx=5
        )

        tk.Label(
            frame,
            text="Deporte"
        ).grid(row=1, column=0)

        self.cbo_deportes = ttk.Combobox(
            frame,
            width=40,
            state="readonly"
        )

        self.cbo_deportes.grid(
            row=1,
            column=1,
            padx=5
        )

        tk.Button(
            frame,
            text="Inscribir",
            command=self.guardar
        ).grid(
            row=2,
            column=0,
            columnspan=2,
            pady=10
        )

        self.tabla = ttk.Treeview(
            self.ventana,
            columns=(
                "ID",
                "Socio",
                "Deporte",
                "Fecha"
            ),
            show="headings"
        )

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Socio", text="Socio")
        self.tabla.heading("Deporte", text="Deporte")
        self.tabla.heading("Fecha", text="Fecha")

        self.tabla.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    def cargar_datos(self):

        self.socios = Socio.obtener_activos()

        lista_socios = []

        for socio in self.socios:

            lista_socios.append(
                f"{socio.IdSocio} - {socio.Apellido}, {socio.Nombre}"
            )

        self.cbo_socios["values"] = lista_socios

        self.deportes = Deporte.obtener_combo()

        lista_deportes = []

        for deporte in self.deportes:

            lista_deportes.append(
                f"{deporte.IdDeporte} - {deporte.Nombre}"
            )

        self.cbo_deportes["values"] = lista_deportes

        self.cargar_tabla()

    def cargar_tabla(self):

        for fila in self.tabla.get_children():

            self.tabla.delete(fila)

        inscripciones = Inscripcion.obtener_todas()

        for inscripcion in inscripciones:

            self.tabla.insert(
                "",
                tk.END,
                values=(
                    inscripcion.IdInscripcion,
                    inscripcion.Socio,
                    inscripcion.Deporte,
                    inscripcion.FechaInscripcion
                )
            )

    def guardar(self):

        if not self.cbo_socios.get():

            messagebox.showwarning(
                "Aviso",
                "Seleccione un socio"
            )

            return

        if not self.cbo_deportes.get():

            messagebox.showwarning(
                "Aviso",
                "Seleccione un deporte"
            )

            return

        id_socio = int(
            self.cbo_socios.get().split("-")[0].strip()
        )

        id_deporte = int(
            self.cbo_deportes.get().split("-")[0].strip()
        )

        Inscripcion.agregar(
            id_socio,
            id_deporte
        )

        self.cargar_tabla()

        messagebox.showinfo(
            "Correcto",
            "Inscripción registrada"
        )