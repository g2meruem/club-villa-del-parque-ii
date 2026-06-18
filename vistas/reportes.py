import tkinter as tk

from modelos.pago import Pago
from modelos.reportes import Reporte


class VentanaReportes:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title(
            "Reportes y Estadísticas"
        )

        self.ventana.geometry(
            "700x650"
        )

        self.cargar_datos()

    def cargar_datos(self):

        total = Reporte.total_recaudado()

        total_invitados = Reporte.total_invitados()

        cantidad_socios = Reporte.cantidad_socios()

        cantidad_inscripciones = Reporte.cantidad_inscripciones()

        cantidad_invitados = Reporte.cantidad_invitados()

        pagos_mes = Reporte.pagos_mes_actual()

        deporte_popular = Reporte.deporte_mas_popular()

        tk.Label(
            self.ventana,
            text="CLUB VILLA DEL PARQUE II",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        tk.Label(
            self.ventana,
            text="RENDICIÓN Y ESTADÍSTICAS",
            font=("Arial", 14)
        ).pack(pady=5)

        tk.Label(
            self.ventana,
            text=f"Socios Activos: {cantidad_socios}"
        ).pack(pady=3)

        tk.Label(
            self.ventana,
            text=f"Inscripciones Deportivas: {cantidad_inscripciones}"
        ).pack(pady=3)

        tk.Label(
            self.ventana,
            text=f"Invitados Registrados: {cantidad_invitados}"
        ).pack(pady=3)

        tk.Label(
            self.ventana,
            text=f"Pagos Registrados Este Mes: {pagos_mes}"
        ).pack(pady=3)

        tk.Label(
            self.ventana,
            text=f"Total Recaudado por Socios: ${total}"
        ).pack(pady=3)

        tk.Label(
            self.ventana,
            text=f"Total Recaudado por Invitados: ${total_invitados}"
        ).pack(pady=3)

        if deporte_popular:

            tk.Label(
                self.ventana,
                text=f"Deporte Más Popular: {deporte_popular[0]} ({deporte_popular[1]} inscripciones)"
            ).pack(pady=10)

        tk.Label(
            self.ventana,
            text="RECAUDACIÓN POR CONCEPTO",
            font=("Arial", 12, "bold")
        ).pack(pady=10)

        conceptos = Reporte.recaudacion_por_concepto()

        for concepto in conceptos:

            tk.Label(
                self.ventana,
                text=f"{concepto[0]}: ${concepto[1]}"
            ).pack()

        tk.Label(
            self.ventana,
            text="SOCIOS POR DEPORTE",
            font=("Arial", 12, "bold")
        ).pack(pady=15)

        deportes = Reporte.socios_por_deporte()

        for deporte in deportes:

            tk.Label(
                self.ventana,
                text=f"{deporte[0]}: {deporte[1]} socios"
            ).pack()

        tk.Label(
            self.ventana,
            text="INVITADOS POR DEPORTE",
            font=("Arial", 12, "bold")
        ).pack(pady=15)

        invitados = Reporte.invitados_por_deporte()

        for invitado in invitados:

            tk.Label(
                self.ventana,
                text=f"{invitado[0]}: {invitado[1]} invitados"
            ).pack()