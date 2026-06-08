# Sistema de Gestión Deportiva Web - Club Villa del Parque II

## Descripción

Sistema web de gestión administrativa para el Club Deportivo Villa del Parque II, desarrollado con Python, Flask y Microsoft SQL Server.

El objetivo principal es digitalizar y optimizar la administración del club, permitiendo gestionar socios, deportes, inscripciones, pagos, comprobantes y rendiciones mensuales desde una interfaz web intuitiva y segura.

---

## Objetivos

### Objetivo General

Desarrollar una aplicación web que permita administrar las actividades deportivas y financieras del Club Villa del Parque II.

### Objetivos Específicos

* Gestionar socios, no socios e invitados.
* Administrar disciplinas deportivas.
* Registrar pagos y cuotas.
* Emitir comprobantes.
* Generar rendiciones mensuales.
* Implementar control de acceso mediante usuarios y roles.
* Almacenar la información en Microsoft SQL Server.

---

## Tecnologías Utilizadas

### Backend

* Python 3
* Flask

### Base de Datos

* Microsoft SQL Server
* SQL Server Management Studio (SSMS)

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* Jinja2

### Conectividad

* pyodbc

### Control de Versiones

* Git
* GitHub

---

## Funcionalidades

### Autenticación

* Inicio de sesión.
* Control de acceso por roles.
* Gestión de usuarios autorizados.

### Dashboard

* Resumen de socios activos.
* Pagos registrados.
* Recaudación mensual.
* Accesos rápidos a los módulos principales.

### Gestión de Socios

* Alta de socios.
* Modificación de datos.
* Baja lógica.
* Consulta de información.

### Gestión de Deportes

* Administración de deportes.
* Gestión de cuotas deportivas.
* Consulta de inscriptos.

### Inscripciones

* Asociación de socios a deportes.
* Consulta de inscripciones activas.

### Gestión de Pagos

* Registro de pagos.
* Consulta de historial.
* Control de cuotas.

### Comprobantes

* Generación automática de comprobantes.
* Visualización e impresión.

### Rendición Mensual

* Cantidad de pagos.
* Total recaudado.
* Recaudación por deporte.
* Informes administrativos.

---

## Deportes Gestionados

* ⚽ Fútbol
* 🏀 Básquet
* 🎾 Tenis

---

## Arquitectura del Sistema

Navegador Web
↓
Flask (Backend)
↓
Lógica de Negocio
↓
Microsoft SQL Server

---

## Estructura del Proyecto

```text
club-villa-del-parque-ii/

├── app.py
│
├── config/
│   └── db.py
│
├── routes/
│   ├── auth.py
│   ├── socios.py
│   ├── deportes.py
│   ├── pagos.py
│   └── reportes.py
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   │
│   ├── socios/
│   │   ├── listar.html
│   │   ├── crear.html
│   │   └── editar.html
│   │
│   ├── pagos/
│   │   ├── listar.html
│   │   └── registrar.html
│   │
│   └── reportes/
│       └── mensual.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── img/
│
├── database/
│   └── ClubVillaDelParqueII.sql
│
├── requirements.txt
│
└── README.md
```


---

## Base de Datos

La base de datos utilizará Microsoft SQL Server.

Tablas principales:

* Roles
* Usuarios
* Socios
* Deportes
* Inscripciones
* Pagos
* Comprobantes

Se reutilizará la estructura inicial diseñada para el proyecto, incorporando mejoras progresivas según sea necesario.

---

## Seguridad

El sistema contará con:

* Autenticación mediante usuario y contraseña.
* Control de acceso por roles.
* Restricción de funciones administrativas.
* Protección de sesiones mediante Flask.

---

## Hoja de Ruta del Proyecto

### Fase 1 - Diseño y Preparación

* [X] Definición de requerimientos.
* [X] Diseño de la base de datos.
* [X] Configuración del repositorio GitHub.
* [ ] Configuración del entorno Flask.

### Fase 2 - Base de Datos

* [ ] Creación de la base de datos en SQL Server.
* [ ] Creación de tablas y relaciones.
* [ ] Inserción de datos iniciales.
* [ ] Creación de vistas y procedimientos almacenados.

### Fase 3 - Backend Flask

* [ ] Configuración de Flask.
* [ ] Conexión con SQL Server.
* [ ] Sistema de autenticación.
* [ ] Gestión de sesiones.

### Fase 4 - Gestión de Socios

* [ ] Alta de socios.
* [ ] Modificación de socios.
* [ ] Baja lógica.
* [ ] Búsquedas y filtros.

### Fase 5 - Gestión Deportiva

* [ ] Administración de deportes.
* [ ] Inscripciones.
* [ ] Gestión de cuotas.

### Fase 6 - Pagos

* [ ] Registro de pagos.
* [ ] Historial de movimientos.
* [ ] Comprobantes.

### Fase 7 - Reportes

* [ ] Rendición mensual.
* [ ] Estadísticas.
* [ ] Informes administrativos.

### Fase 8 - Interfaz y Mejoras

* [ ] Diseño responsive con Bootstrap.
* [ ] Validaciones.
* [ ] Mejoras visuales.
* [ ] Optimización general.

### Fase 9 - Documentación

* [ ] Manual de usuario.
* [ ] Diagrama entidad-relación.
* [ ] Documentación técnica.
* [ ] Presentación final.

---

## Estado Actual

🚧 En desarrollo

Versión objetivo: 1.0

---

## Integrantes

* Gastón Toranzo

---

## Licencia

Proyecto académico desarrollado con fines educativos para la materia de Técnicas de programación y Bases de Datos - Año 2026.
