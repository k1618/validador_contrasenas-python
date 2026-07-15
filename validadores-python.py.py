def validar_nombre(nombre):
    return len(nombre.strip()) >= 3


def validar_edad(edad):
    return edad > 0


def validar_correo(correo):
    return "@" in correo and "." in correo.split("@")[-1]


def registrar_usuario():
    """Solicita y valida los datos de un usuario nuevo."""
    nombre = input("Ingrese su nombre: ")
    
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            break
        except ValueError:
            print("Por favor ingrese un número válido.")
    
    correo = input("Ingrese su correo electrónico: ")

    errores = []
    if not validar_nombre(nombre):
        errores.append("El nombre debe tener al menos 3 caracteres.")
    if not validar_edad(edad):
        errores.append("La edad debe ser mayor a 0.")
    if not validar_correo(correo):
        errores.append("El correo electrónico no tiene un formato válido.")

    if not errores:
        print(f"\n¡Registro exitoso! Bienvenido, {nombre}.")
        return {"nombre": nombre, "edad": edad, "correo": correo}
    else:
        print("\nDatos inválidos:")
        for error in errores:
            print(f"  - {error}")
        return None


if __name__ == "__main__":
    registrar_usuario()