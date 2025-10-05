import pytest
from agenda.main import AgendaTelefonica

def test_agregar_contacto_valido():
    agenda = AgendaTelefonica()
    agenda.agregar_contacto("Carlos", "0998765432")
    assert agenda.obtener_contacto("Carlos") == "0998765432"

def test_nombre_invalido():
    agenda = AgendaTelefonica()
    with pytest.raises(ValueError):
        agenda.agregar_contacto("Carlos123", "0998765432")

def test_telefono_invalido():
    agenda = AgendaTelefonica()
    with pytest.raises(ValueError):
        agenda.agregar_contacto("Maria", "123")
