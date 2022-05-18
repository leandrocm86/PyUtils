import pytest
from pyutils.cronometro import Cronometro
from pyutils.sistema import Sistema

def test_leitura():
    saida = Sistema.ler('echo abc; echo def; echo ghi')
    assert all(linha in saida for linha in ['abc', 'def', 'ghi'])

def test_leitura_error():
    saida = Sistema.ler('ofjho0eijf')
    assert 'not found' in saida 

def test_exec():
    Sistema.exec('printf "\n\n"')
    Sistema.exec('echo "  "')

def test_exec_ignora_saida():
    Sistema.exec('echo "Ah!"', True)

def test_exec_fail():
    with pytest.raises(Exception):
        Sistema.exec('ls')

# def test_ler_ok_and_fail():
#     curl = Sistema.ler("curl -H 'Accept: application/vnd.github.v3+json' https://api.github.com/repos/leandrocm86/traffic-monitor/actions/artifacts -u leandrocm86:$GITTOKEN | head -12 | grep created")
#     assert 'ERRO' in curl
#     assert 'created_at' in curl

def test_ler_timeout():
    with pytest.raises(Exception):
        Sistema.ler('sleep 0.3; echo "abc"', timeout=0.2)

def test_exec_timeout():
    Cronometro.start()
    Sistema.exec('sleep 0.2')
    assert Cronometro.check() >= 0.2
    Sistema.execAsync('sleep 0.2')
    assert Cronometro.check() < 0.2
    try:
        Sistema.exec('sleep 1', timeout=0.2)
    except: assert 0.2 <= Cronometro.check() < 0.3

