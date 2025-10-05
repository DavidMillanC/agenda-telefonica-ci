class AgendaTelefonica:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono):
        if not nombre.isalpha():
            raise ValueError("El nombre debe contener solo letras.")
        if not telefono.isdigit() or len(telefono) != 10:
            raise ValueError("El número debe tener exactamente 10 dígitos.")
        self.contactos[nombre] = telefono

    def obtener_contacto(self, nombre):
        return self.contactos.get(nombre, "Contacto no encontrado.")

    def buscar_contacto(self, filtro):
        return {nombre: tel for nombre, tel in self.contactos.items() if filtro.lower() in nombre.lower()}
