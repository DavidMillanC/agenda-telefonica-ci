import re

class AgendaTelefonica:
    def __init__(self):
        self.contactos = []

    def _validar_nombre(self, nombre):
        return bool(re.match(r'^[a-zA-Z\s]+$', nombre.strip()))

    def _validar_numero(self, numero):
        return bool(re.match(r'^\d{10}$', numero))

    def agregar_contacto(self, nombre, numero):
        if not self._validar_nombre(nombre):
            raise ValueError("Error: El nombre solo debe contener letras y espacios.")
        if not self._validar_numero(numero):
            raise ValueError("Error: El número debe contener exactamente 10 dígitos.")
        
        contacto = {"nombre": nombre.strip(), "numero": numero}
        self.contactos.append(contacto)
        return f"Contacto {nombre.strip()} registrado con éxito."

    def obtener_contacto(self, nombre):
        nombre_buscado = nombre.strip().lower()
        for contacto in self.contactos:
            if contacto["nombre"].lower() == nombre_buscado:
                return contacto['numero']
        return None

    def buscar_contacto(self, termino_busqueda):
        termino = termino_busqueda.strip().lower()
        resultados = {contacto['nombre']: contacto['numero'] for contacto in self.contactos if termino in contacto['nombre'].lower()}
        return resultados
    
    def eliminar_contacto(self, nombre):
        nombre_buscado = nombre.strip().lower()
        msg="Contacto no encontrado"
        for contacto in self.contactos:
            if contacto['nombre'].lower() == nombre_buscado:
                self.contactos.remove(contacto)
                msg=f"Contacto {nombre.strip()} eliminado con éxito."
                return msg