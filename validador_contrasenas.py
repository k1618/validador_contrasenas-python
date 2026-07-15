def validar_contrasena(contrasena):
    """
    Valida que la contraseña cumpla con requisitos mínimos de seguridad.
    Retorna una lista de errores (vacía si todo está bien).
    """
    errores = []
    
    if len(contrasena) < 8:
        errores.append("Debe tener al menos 8 caracteres.")
    if not any(c.isupper() for c in contrasena):
        errores.append("Debe incluir al menos una letra mayúscula.")
    if not any(c.islower() for c in contrasena):
        errores.append("Debe incluir al menos una letra minúscula.")
    if not any(c.isdigit() for c in contrasena):
        errores.append("Debe incluir al menos un número.")
    if not any(c in "!@#$%^&*()_+-=" for c in contrasena):
        errores.append("Debe incluir al menos un carácter especial (!@#$%^&* etc).")
    
    return errores


def main():
    while True:
        nombre_usuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        errores = validar_contrasena(contrasena)

        if not errores:
            print(f"¡Acceso concedido, {nombre_usuario}!")
            break
        else:
            print("\nLa contraseña no es válida:")
            for error in errores:
                print(f"  - {error}")
            print()  # línea en blanco antes de reintentar


if __name__ == "__main__":
    main()
