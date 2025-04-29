# Práctica Formativa Obligatoria 1 - Programación sobre Redes

**Título:** Implementación de un Chat Básico Cliente-Servidor con Sockets y Base de Datos
**Docente:** Alan Portillo
**Nombre:** Soledad Aldao  
**Materia:** Programación sobre Redes  
**Carrera:** Tecnicatura Superior en Desarrollo de Software  
**Año:** 2025

---

## Objetivo

Configurar un servidor de sockets en Python que reciba mensajes de clientes, los almacene en una base de datos SQLite y envíe confirmaciones, aplicando buenas prácticas de modularización y manejo de errores.

---

## Estructura de carpetas del proyecto

chat/
├── client.py # Cliente TCP que envía mensajes al servidor
├── server.py # Servidor TCP que recibe y guarda los mensajes
├── db.py # Módulo de base de datos SQLite
├── utils.py # Archivo de utilidades para manejo de errores y timestamps
├── chat.db # Base de datos SQLite generada automáticamente
└── README.md # Documentación del proyecto

## Para probar el sistema

1. **Clonar el repositorio**

```bash
git clone https://github.com/solealdao/pfo1-aldao.git
cd pfo1-aldao/chat
```

2. **Ejecutar el servidor en una terminal**

```bash
python3 server.py
```

3. **Ejecutar el cliente en otra terminal**

```bash
python3 client.py
```
