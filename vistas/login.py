import tkinter as tk
from tkinter import messagebox

from modelos.usuario import Usuario
from vistas.dashboard import VentanaDashboard

class VentanaLogin:

    def __init__(self):

        self.ventana = tk.Tk()

        self.ventana.title(
            "Club Villa del Parque II"
        )

        self.ventana.geometry("400x250")

        self.crear_componentes()

        self.ventana.mainloop()

    def crear_componentes(self):

        tk.Label(
            self.ventana,
            text="Club Villa del Parque II",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        tk.Label(
            self.ventana,
            text="Usuario"
        ).pack()

        self.txt_usuario = tk.Entry(
            self.ventana
        )

        self.txt_usuario.pack()

        tk.Label(
            self.ventana,
            text="Contraseña"
        ).pack()

        self.txt_password = tk.Entry(
            self.ventana,
            show="*"
        )

        self.txt_password.pack()

        tk.Button(
            self.ventana,
            text="Ingresar",
            command=self.ingresar
        ).pack(pady=20)

    def ingresar(self):

        usuario = self.txt_usuario.get()

        password = self.txt_password.get()

        resultado = Usuario.validar(
            usuario,
            password
        )

        if resultado:

            self.ventana.destroy()
            VentanaDashboard(
                resultado.Usuario,
                resultado.NombreRol
            )


        else:

            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos"
            )