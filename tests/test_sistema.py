import pytest
try:
   import sistema as sis
except ImportError:
   import PyUtils.sistema as sis

def test_leitura():
    saida = sis.ler('ls')
    assert all(linha in saida for linha in ['strings.py', 'sistema.py'])

def test_exec():
    sis.exec('echo "  "')

def test_exec_ignora_saida():
    sis.exec('echo "Ah!"', True)

def test_exec_fail():
    with pytest.raises(Exception):
        sis.exec('ls')