# Validadores en Python

Colección de scripts en Python que validan datos de usuario (contraseñas y registro), 
con manejo de errores y retroalimentación clara para el usuario.

## 📋 Contenido

### `validador_contrasenas.py`
Valida que una contraseña cumpla con requisitos de seguridad:
- Mínimo 8 caracteres
- Al menos una letra mayúscula
- Al menos una letra minúscula
- Al menos un número
- Al menos un carácter especial

Si la contraseña no cumple, muestra exactamente qué requisitos faltan y permite reintentar.

**Cómo ejecutarlo:**
```bash
python validador_contrasenas.py
```

### `validador_registro.py`
Simula el registro de un nuevo usuario, validando:
- Nombre (mínimo 3 caracteres)
- Edad (debe ser un número positivo)
- Correo electrónico (formato básico válido)

Maneja errores si el usuario ingresa texto donde se espera un número, y devuelve 
los datos validados en un diccionario para su posible uso posterior (ej. guardarlos 
en una base de datos).

**Cómo ejecutarlo:**
```bash
python validador_registro.py
```

## 🎯 Objetivo del proyecto

Practicar validación de datos, manejo de errores (`try/except`), estructuración de 
código en funciones reutilizables, y buenas prácticas básicas de Python.

## 🚀 Posibles mejoras futuras

- Conectar `validador_registro.py` a una base de datos real (SQLite)
- Agregar pruebas unitarias con `unittest` o `pytest`
- Crear una interfaz gráfica simple con `tkinter`

## 🛠️ Tecnologías

- Python 3

## 👤 Autor

Dilan Eduardo Martínez Castro — [github.com/k1618](https://github.com/k1618)
