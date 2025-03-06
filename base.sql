/* 2025-02-27 23:35:19 [4 ms] */ 
CREATE DATABASE clientes_db;
/* 2025-02-27 23:35:20 [3 ms] */ 
USE clientes_db;
/* 2025-02-27 23:35:22 [10 ms] */ 
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    tipo_documento VARCHAR(20),
    numero_documento VARCHAR(20),
    ciudad VARCHAR(50),
    direccion VARCHAR(100),
    telefono VARCHAR(15),
    email VARCHAR(50)
);
