import sistema as sis
import pytest

def test_leitura():
    saida = sis.ler('ls')
    assert all(linha in saida for linha in ['sistema.py', 'test_sistema.py'])

def test_exec():
    sis.exec('echo "  "')

def test_exec_ignora_saida():
    sis.exec('echo "Ah!"', True)

def test_exec_fail():
    with pytest.raises(Exception):
        sis.exec('ls')