import pytest
from pyutils.clock import Clock
from pyutils.system import System


def test_read():
    output = System.read('echo abc; echo def; echo ghi')
    assert all(line in output for line in ['abc', 'def', 'ghi'])


def test_read_error():
    output = System.read('ofjho0eijf')
    assert 'not found' in output 


def test_exec():
    System.exec('printf "\n\n"')
    System.exec('echo "  "')


def test_exec_ignora_output():
    System.exec('echo "Ah!"', True)


def test_exec_fail():
    with pytest.raises(Exception):
        System.exec('ls')


def test_read_timeout():
    with pytest.raises(Exception):
        System.read('sleep 0.3; echo "abc"', timeout=0.2)


def test_exec_timeout():
    Clock.start()
    System.exec('sleep 0.2')
    assert Clock.check() >= 0.2
    System.exec_async('sleep 0.2')
    assert Clock.check() < 0.2
    try:
        System.exec('sleep 1', timeout=0.2)
    except: assert 0.2 <= Clock.check() < 0.3


def test_file_path():
    assert '/scripts/mods/PyUtils/tests/' in System.file_path(__file__)

