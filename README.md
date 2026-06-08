# Sistema de Gestión Deportiva - Club Villa del Parque II

## Descripción

Sistema de gestión administrativa desarrollado en Python para el Club Deportivo Villa del Parque II.

La aplicación permitirá administrar socios, actividades deportivas, inscripciones, pagos, comprobantes y rendiciones mensuales mediante una interfaz gráfica desarrollada con Tkinter y almacenamiento de datos en Microsoft SQL Server.

---

# Objetivos

## Objetivo General

Desarrollar una aplicación de escritorio que permita gestionar de manera eficiente la administración del Club Villa del Parque II.

## Objetivos Específicos

* Gestionar socios, no socios e invitados.
* Administrar disciplinas deportivas.
* Registrar pagos y cuotas.
* Emitir comprobantes.
* Generar rendiciones mensuales.
* Implementar control de acceso mediante usuarios y roles.
* Almacenar la información en Microsoft SQL Server.

---

# Tecnologías Utilizadas

## Lenguaje

* Python 3

## Base de Datos

* Microsoft SQL Server
* SQL Server Management Studio (SSMS)

## Interfaz Gráfica

* Tkinter
* ttk (Treeview)

## Conectividad

* pyodbc

## Control de Versiones

* Git
* GitHub

---

# Funcionalidades

## Autenticación

* Inicio de sesión.
* Gestión de usuarios.
* Control de acceso por roles.

## Gestión de Socios

* Alta de socios.
* Modificación de datos.
* Baja lógica.
* Consulta y búsqueda.

## Gestión Deportiva

* Administración de deportes.
* Gestión de cuotas.
* Consulta de inscriptos.

## Inscripciones

* Asociación de socios a deportes.
* Consulta de inscripciones activas.

## Gestión de Pagos

* Registro de pagos.
* Consulta de historial.
* Control de cuotas.

## Comprobantes

* Generación automática de comprobantes.
* Visualización por pantalla.

## Rendición Mensual

* Total recaudado.
* Cantidad de pagos.
* Recaudación por actividad.
* Estadísticas administrativas.

---

# Deportes Gestionados

* ⚽ Fútbol
* 🏀 Básquet
* 🎾 Tenis

---

# Arquitectura del Sistema

Interfaz Gráfica (Tkinter)
↓
Lógica de Negocio (Python)
↓
Microsoft SQL Server

---

# Estructura del Proyecto

```text
club-villa-del-parque-ii/

├── main.py
│
├── config/
│   └── conexion.py
│
├── vistas/
│   ├── login.py
│   ├── dashboard.py
│   ├── socios.py
│   ├── deportes.py
│   ├── pagos.py
│   └── reportes.py
│
├── modelos/
│   ├── usuario.py
│   ├── socio.py
│   ├── deporte.py
│   └── pago.py
│
├── database/
│   └── ClubVillaDelParqueII.sql
│
├── assets/
│   └── logo.png
│
├── requirements.txt
│
└── README.md
```

---

# Base de Datos

La aplicación utilizará Microsoft SQL Server como sistema gestor de base de datos.

Tablas principales:

* Roles
* Usuarios
* Socios
* Deportes
* Inscripciones
* Pagos
* Comprobantes

---

# Seguridad

El sistema contará con:

* Autenticación mediante usuario y contraseña.
* Control de acceso por roles.
* Restricción de funciones administrativas.
* Protección de operaciones sensibles.

---

# Hoja de Ruta del Proyecto

## Fase 1 - Diseño

* [X] Definición de requerimientos.
* [X] Diseño de base de datos.
* [X] Configuración del repositorio.

## Fase 2 - Base de Datos

* [ ] Creación de tablas.
* [ ] Relaciones y restricciones.
* [ ] Datos iniciales.
* [ ] Procedimientos almacenados.

## Fase 3 - Infraestructura

* [ ] Configuración del proyecto Python.
* [ ] Conexión con SQL Server.
* [ ] Estructura modular.

## Fase 4 - Login

* [ ] Inicio de sesión.
* [ ] Validación de usuarios.
* [ ] Gestión de roles.

## Fase 5 - Gestión de Socios

* [ ] Alta.
* [ ] Modificación.
* [ ] Baja.
* [ ] Búsqueda.

## Fase 6 - Gestión Deportiva

* [ ] Administración de deportes.
* [ ] Inscripciones.
* [ ] Consulta de participantes.

## Fase 7 - Gestión de Pagos

* [ ] Registro de pagos.
* [ ] Historial.
* [ ] Comprobantes.

## Fase 8 - Reportes

* [ ] Rendición mensual.
* [ ] Estadísticas.
* [ ] Informes.

## Fase 9 - Finalización

* [ ] Pruebas.
* [ ] Manual de usuario.
* [ ] Documentación técnica.
* [ ] Presentación final.

---

# Estado del Proyecto

🚧 En desarrollo

Versión objetivo: 1.0

---

# Integrante

* Gastón Toranzo

---

# Licencia

Proyecto académico desarrollado con fines educativos para la materia de Programación y Bases de Datos - Año 2026.
