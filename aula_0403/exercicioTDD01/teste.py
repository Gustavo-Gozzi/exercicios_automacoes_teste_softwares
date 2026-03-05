import pytest 
from codigo import obter_categoria

def test_infantil_A():
    idades = [5, 6, 7]
    for i in idades:
        assert obter_categoria(i) == 'Infantil A'

def test_infantil_B():
    idades = [8, 9, 10]
    for i in idades:
        assert obter_categoria(i) == 'Infantil B'

def test_juvenil_A():
    idades = [11, 12, 13]
    for i in idades:
        assert obter_categoria(i) == 'Juvenil A'

def test_juvenil_B():
    idades = [14, 15, 16, 17]
    for i in idades:
        assert obter_categoria(i) == 'Juvenil B'

def test_senior():
    for i in range(18,100):
        assert obter_categoria(i) == 'Sênior'

def test_idade_menor_5():
    for i in range(1, 5):
        assert obter_categoria(i) == False

   
def test_idade_negativa():
    for i in range(-100, 0):
        assert obter_categoria(i) == 'Erro Idade Negativa'
