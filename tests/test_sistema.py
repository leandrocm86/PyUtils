import pytest
try:
   import sistema as sis
except ImportError:
   import PyUtils.sistema as sis

def test_leitura():
    saida = sis.ler('ls')
    assert all(linha in saida for linha in ['strings.py', 'sistema.py'])

def test_leitura_error():
    saida = sis.ler('ofjho0eijf')
    assert 'command not found' in saida 

def test_exec():
    sis.exec('find -name ijisjwijs')
    sis.exec('echo "  "')

def test_exec_ignora_saida():
    sis.exec('echo "Ah!"', True)

def test_exec_fail():
    with pytest.raises(Exception):
        sis.exec('ls')
