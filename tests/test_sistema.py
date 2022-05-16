import pytest
from pyutils import sistema as sis

def test_leitura():
    saida = sis.ler('ls pyutils')
    assert all(linha in saida for linha in ['strings.py', 'sistema.py'])

def test_leitura_error():
    saida = sis.ler('ofjho0eijf')
    assert 'not found' in saida 

def test_exec():
    sis.exec('find -name ijisjwijs')
    sis.exec('echo "  "')

def test_exec_ignora_saida():
    sis.exec('echo "Ah!"', True)

def test_exec_fail():
    with pytest.raises(Exception):
        sis.exec('ls')

def test_ler_ok_and_fail():
    curl = sis.ler("curl -H 'Accept: application/vnd.github.v3+json' https://api.github.com/repos/leandrocm86/traffic-monitor/actions/artifacts -u leandrocm86:$GITTOKEN | head -12 | grep created")
    assert 'ERRO' in curl
    assert 'created_at' in curl
