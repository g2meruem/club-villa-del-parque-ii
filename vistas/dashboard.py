import tkinter as tk
from vistas.socios import VentanaSocios

class VentanaDashboard:
    def abrir_socios(self):

        VentanaSocios()
        
    def __init__(self, usuario, rol):

        self.ventana = tk.Tk()

        self.ventana.title(
            "Dashboard - Club Villa del Parque II"
        )

        self.ventana.geometry("600x400")

        self.usuario = usuario
        self.rol = rol

        self.crear_componentes()

        self.ventana.mainloop()

    def crear_componentes(self):

        titulo = tk.Label(
            self.ventana,
            text="CLUB VILLA DEL PARQUE II",
            font=("Arial", 18, "bold")
        )

        titulo.pack(pady=10)

        lbl_usuario = tk.Label(
            self.ventana,
            text=f"Usuario: {self.usuario}"
        )

        lbl_usuario.pack()

        lbl_rol = tk.Label(
            self.ventana,
            text=f"Rol: {self.rol}"
        )

        lbl_rol.pack(pady=10)

        tk.Button(
            self.ventana,
            text="Gestión de Socios",
            width=30,
            command=self.abrir_socios
        ).pack(pady=5)

        tk.Button(
            self.ventana,
            text="Gestión de Deportes",
            width=30
        ).pack(pady=5)

        tk.Button(
            self.ventana,
            text="Pagos",
            width=30
        ).pack(pady=5)

        tk.Button(
            self.ventana,
            text="Reportes",
            width=30
        ).pack(pady=5)

        tk.Button(
            self.ventana,
            text="Salir",
            width=30,
            command=self.ventana.destroy
        ).pack(pady=20)