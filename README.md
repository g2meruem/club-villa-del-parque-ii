# Sistema de Gestión Deportiva - Club Villa del Parque II

## Descripción

Este proyecto consiste en el desarrollo de un sistema administrativo para el **Club Deportivo Villa del Parque II**, implementado en **Python** y **SQL**, con el objetivo de facilitar la gestión de socios, actividades deportivas, cuotas, pagos y rendiciones mensuales.

El sistema busca digitalizar los procesos administrativos del club, permitiendo un control más eficiente de la información y una mejor organización de los recursos.

---

## Objetivos del Proyecto

* Administrar socios, no socios e invitados.
* Gestionar inscripciones a actividades deportivas.
* Controlar cuotas sociales y deportivas.
* Emitir comprobantes de pago.
* Generar informes y rendiciones mensuales.
* Implementar acceso restringido mediante usuarios y roles.
* Almacenar información de manera segura utilizando una base de datos SQL.

---

## Deportes Incluidos

El sistema contempla inicialmente la gestión de las siguientes disciplinas:

* ⚽ Fútbol
* 🏀 Básquet
* 🎾 Tenis

---

## Funcionalidades Principales

### Gestión de Usuarios

* Inicio de sesión.
* Control de acceso por roles.
* Administración de usuarios autorizados.

### Gestión de Socios

* Alta de socios.
* Modificación de datos.
* Baja lógica de registros.
* Consulta de información.

### Gestión de No Socios e Invitados

* Registro de participantes ocasionales.
* Control de acceso a actividades.

### Gestión de Deportes

* Inscripción a disciplinas.
* Consulta de participantes por deporte.
* Control de cuotas deportivas.

### Gestión de Pagos

* Registro de pagos.
* Historial de movimientos.
* Control de cuotas vencidas.
* Consulta de estados de cuenta.

### Emisión de Comprobantes

* Generación de comprobantes por pantalla.
* Numeración automática.
* Registro de fecha y concepto del pago.

### Rendición de Cuentas

* Ingresos mensuales.
* Recaudación por actividad deportiva.
* Reportes de pagos realizados.
* Estadísticas administrativas.

---

## Tecnologías Utilizadas

### Lenguajes

* Python

### Base de Datos

* Sql MS

### Herramientas

* Git
* GitHub
* Visual Studio Code

---

## Estructura Inicial del Proyecto

```text
club-villa-del-parque-ii/
│
├── database/
│   ├── schema.sql
│   └── club.db
│
├── src/
│   ├── main.py
│   ├── login.py
│   ├── socios.py
│   ├── deportes.py
│   ├── pagos.py
│   ├── invitados.py
│   └── reportes.py
│
├── docs/
│   ├── proyecto.pdf
│   ├── diagrama_er.png
│   └── manual_usuario.pdf
│
├── README.md
└── requirements.txt
```

---

## Modelo de Datos

El sistema estará compuesto inicialmente por las siguientes entidades:

* Usuarios
* Socios
* Deportes
* Inscripciones
* Pagos
* Invitados

Estas tablas estarán relacionadas para garantizar la integridad y consistencia de la información.

---

## Seguridad

El sistema contará con:

* Autenticación mediante usuario y contraseña.
* Roles de acceso.
* Restricción de funciones administrativas.
* Protección de información sensible.

---

## Estado del Proyecto

🚧 En desarrollo

### Próximas etapas

* [X] Diseño de base de datos.
* [X] Creación del diagrama entidad-relación.
* [ ] Implementación del sistema de login.
* [ ] Gestión de socios.
* [ ] Gestión de deportes.
* [ ] Gestión de pagos.
* [ ] Emisión de comprobantes.
* [ ] Rendición mensual.
* [ ] Pruebas y documentación final.

---

## Integrantes

* Gastón Toranzo

---

## Licencia

Proyecto académico desarrollado con fines educativos para la materia de Técnicas de programación y Bases de Datos - IFTS 16° - Año 2026.
