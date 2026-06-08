-- ====================================
-- CREACION BASE DE DATOS
-- CLUB VILLA DEL PARQUE II
-- ====================================

CREATE DATABASE ClubVillaDelParqueII;
GO

USE ClubVillaDelParqueII;
GO

-- ====================================
-- ROLES
-- ====================================

CREATE TABLE Roles(
IdRol INT IDENTITY(1,1) PRIMARY KEY,
NombreRol VARCHAR(50) NOT NULL UNIQUE
);

-- ====================================
-- USUARIOS
-- ====================================

CREATE TABLE Usuarios(
IdUsuario INT IDENTITY(1,1) PRIMARY KEY,
Usuario VARCHAR(50) NOT NULL UNIQUE,
PasswordHash VARCHAR(255) NOT NULL,
IdRol INT NOT NULL,

```
CONSTRAINT FK_Usuarios_Roles
    FOREIGN KEY(IdRol)
    REFERENCES Roles(IdRol)
```

);

-- ====================================
-- SOCIOS
-- ====================================

CREATE TABLE Socios(
IdSocio INT IDENTITY(1,1) PRIMARY KEY,

```
Nombre VARCHAR(50) NOT NULL,
Apellido VARCHAR(50) NOT NULL,

DNI VARCHAR(15) NOT NULL UNIQUE,

Telefono VARCHAR(30),
Direccion VARCHAR(100),

FechaAlta DATE NOT NULL DEFAULT GETDATE(),

Activo BIT NOT NULL DEFAULT 1
```

);

-- ====================================
-- DEPORTES
-- ====================================

CREATE TABLE Deportes(
IdDeporte INT IDENTITY(1,1) PRIMARY KEY,

```
Nombre VARCHAR(50) NOT NULL UNIQUE,

CuotaMensual DECIMAL(10,2) NOT NULL
```

);

-- ====================================
-- INSCRIPCIONES
-- ====================================

CREATE TABLE Inscripciones(
IdInscripcion INT IDENTITY(1,1) PRIMARY KEY,

```
IdSocio INT NOT NULL,
IdDeporte INT NOT NULL,

FechaInscripcion DATE NOT NULL DEFAULT GETDATE(),

Estado VARCHAR(20) NOT NULL DEFAULT 'Activa',

CONSTRAINT FK_Inscripciones_Socios
    FOREIGN KEY(IdSocio)
    REFERENCES Socios(IdSocio),

CONSTRAINT FK_Inscripciones_Deportes
    FOREIGN KEY(IdDeporte)
    REFERENCES Deportes(IdDeporte)
```

);

-- ====================================
-- TIPOS DE PAGO
-- ====================================

CREATE TABLE TiposPago(
IdTipoPago INT IDENTITY(1,1) PRIMARY KEY,

```
NombreTipo VARCHAR(50) NOT NULL UNIQUE
```

);

-- ====================================
-- PAGOS
-- ====================================

CREATE TABLE Pagos(
IdPago INT IDENTITY(1,1) PRIMARY KEY,

```
IdSocio INT NOT NULL,
IdTipoPago INT NOT NULL,

Concepto VARCHAR(100) NOT NULL,

Importe DECIMAL(10,2) NOT NULL,

FechaPago DATETIME NOT NULL DEFAULT GETDATE(),

CONSTRAINT FK_Pagos_Socios
    FOREIGN KEY(IdSocio)
    REFERENCES Socios(IdSocio),

CONSTRAINT FK_Pagos_TiposPago
    FOREIGN KEY(IdTipoPago)
    REFERENCES TiposPago(IdTipoPago)
```

);

-- ====================================
-- COMPROBANTES
-- ====================================

CREATE TABLE Comprobantes(
IdComprobante INT IDENTITY(1,1) PRIMARY KEY,

```
IdPago INT NOT NULL UNIQUE,

FechaEmision DATETIME NOT NULL DEFAULT GETDATE(),

CONSTRAINT FK_Comprobantes_Pagos
    FOREIGN KEY(IdPago)
    REFERENCES Pagos(IdPago)
```

);
GO