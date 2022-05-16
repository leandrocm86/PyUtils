import pytest
from pyutils.sistema import Sistema

def test_leitura():
    saida = Sistema.ler('ls pyutils')
    assert all(linha in saida for linha in ['strings.py', 'sistema.py'])

def test_leitura_error():
    saida = Sistema.ler('ofjho0eijf')
    assert 'not found' in saida 

def test_exec():
    Sistema.exec('find -name ijisjwijs')
    Sistema.exec('echo "  "')

def test_exec_ignora_saida():
    Sistema.exec('echo "Ah!"', True)

def test_exec_fail():
    with pytest.raises(Exception):
        Sistema.exec('ls')

def test_ler_ok_and_fail():
    curl = Sistema.ler("curl -H 'Accept: application/vnd.github.v3+json' https://api.github.com/repos/leandrocm86/traffic-monitor/actions/artifacts -u leandrocm86:$GITTOKEN | head -12 | grep created")
    assert 'ERRO' in curl
    assert 'created_at' in curl
