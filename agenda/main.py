import re  
class AgendaTelefonica:
    def __init__(self):
        self.contactos = {}

    def obtener_contacto(self, nombre):
                if not self.contactos:
                    return self.contactos.get(nombre, "Contacto no encontrado.")
                return "\n".join([f"{nombre}: {telefono}" for nombre, telefono in self.contactos.items()])

    def buscar_contacto(self, filtro):
        return {nombre: tel for nombre, tel in self.contactos.items() if filtro.lower() in nombre.lower()}

    def agregar_contacto(self, nombre, telefono):
        nombre = nombre.strip()
        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+", nombre):
            raise ValueError("El nombre debe contener solo letras y espacios.")
        if not telefono.isdigit() or len(telefono) != 10:
            raise ValueError("El número debe tener exactamente 10 dígitos.")
        if nombre in self.contactos:
            raise ValueError("El contacto ya existe.")
        self.contactos[nombre] = telefono


    def eliminar_contacto(self, nombre):
        nombre = nombre.strip()
        if nombre in self.contactos:
            del self.contactos[nombre]
            return f"Contacto '{nombre}' eliminado."
        else:
            return "Contacto no encontrado."

