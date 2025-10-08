import pytest
from agenda.main import AgendaTelefonica

def test_agregar_contacto_valido():
    agenda = AgendaTelefonica()
    agenda.agregar_contacto("Carlos", "0998765432")
    agenda.obtener_contacto("Carlos") == "0998765432"
    assert agenda.obtener_contacto("Carlos") == "0998765432"
""" 
def test_agregar_contacto_valido():
    agenda = AgendaTelefonica()
    agenda.agregar_contacto("Carlos", "00")
    assert agenda.obtener_contacto("Carlos") == "0998765432" """

def test_nombre_invalido():
    agenda = AgendaTelefonica()
    with pytest.raises(ValueError):
        agenda.agregar_contacto("Carlos123", "0998765432")

def test_telefono_invalido():
    agenda = AgendaTelefonica()
    with pytest.raises(ValueError):
        agenda.agregar_contacto("Maria", "123")

def test_buscar_contacto():
    agenda = AgendaTelefonica()
    agenda.agregar_contacto("Carlos", "0998765432")
    agenda.agregar_contacto("Carla", "0987654321")
    resultado = agenda.buscar_contacto("Car")
    assert "Carlos" in resultado
    assert "Carla" in resultado

def test_eliminar_contacto():
    agenda = AgendaTelefonica()
    agenda.agregar_contacto("Carlos", "0998765432")
    mensaje = agenda.eliminar_contacto("Carlos")
    assert mensaje == "Contacto Carlos eliminado con éxito."
    assert agenda.obtener_contacto("Carlos") is None

