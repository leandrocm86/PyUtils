from pyutils.strings import String

def test_linha_com():
    texto = String('abaxi ácido\nbanana doce\nlaranja doce\nmorango bom')
    assert texto.linha_com('banana') == 'banana doce'
    assert texto.linha_com('banana', 'doce') == 'banana doce'
    assert texto.linha_com('abacate') == None

def test_linhas_com():
    texto = String('abaxi ácido\nbanana doce\nlaranja doce\nmorango bom')
    assert texto.linhas_com('doce') == ['banana doce', 'laranja doce']
    assert texto.linhas_com('azedo') == []

def test_celula_com():
    texto = String('↳ Corsair Corsair STRAFE Gaming Keyboard Consumer Control   id=19   [slave  keyboard (3)]')
    assert texto.celula_com('id=') == 'id=19'

def test_desde_ate():
    texto = String('↳ Corsair Corsair STRAFE Gaming Keyboard Consumer Control   id=19   [slave  keyboard (3)]')
    assert texto.desde('id=').ate(' ') == '19'
    assert texto.desde_incluso('[').ate_incluso(']') == '[slave  keyboard (3)]'
    assert texto.desde('STRAFE').ate('abcd').ate('Control') == ' Gaming Keyboard Consumer '

def test_desde_ultimo_ate_ultimo():
    s = String('/home/l86/scripts/teste.py')
    assert s.desde_ultimo('/') == 'teste.py'
    assert s.ate_ultimo('/', fim_incluso=True) == '/home/l86/scripts/'

def test_strip():
    original = String(' teste123\n')
    alteracao = original.strip()
    assert original == ' teste123\n'
    assert alteracao == 'teste123'

def test_aparar():
    mutavel = String(' teste123\n')
    mutavel.aparar()
    assert mutavel.val == 'teste123'

def test_replace():
    original = String('abacaxi')
    alteracao = original.replace('a', 'e')
    assert original == 'abacaxi'
    assert alteracao == 'ebecexi'

def test_trocar():
    mutavel = String('abacaxi')
    mutavel.trocar('a', 'e')
    assert mutavel == 'ebecexi'

def test_strtodate():
    data = String.strtodate('05/01/1986')
    assert data.year == 1986
    assert data.month == 1
    assert data.day == 5

def test_todate():
    data = String('05/01/1986 13:30').todate('%d/%m/%Y %H:%M')
    assert data.year == 1986
    assert data.month == 1
    assert data.day == 5
    assert data.hour == 13
    assert data.minute == 30

def test_fromdate():
    data = String('05/01/1986 13:30:59').todate('%d/%m/%Y %H:%M:%S')
    assert String.fromdate(data, '%d-%m-%Y %H:%M') == '05-01-1986 13:30'
    data = String.strtodate('31/12/2000')
    assert String.fromdate(data, '%d-%m-%Y - %H:%M') == '31-12-2000 - 00:00'
    assert String.fromdate(format='%H:%M:%S,%f') != '00:00:00.000000'

def test_hash():
    mapa = dict([])
    mapa[String('teste')] = 1
    mapa[String('teste2')] = 2
    assert mapa[String('teste')] == 1
    assert mapa['teste2'] == 2
    
def test_split():
    assert String('abc\ndef\n').split('\n') == ['abc', 'def', '']
    assert String('').split('\n') == ['']
    assert String('\n').split('\n') == ['', '']

def test_splitlines():
    assert String('abc\ndef\n').splitlines() == ['abc', 'def']
    assert String('').splitlines() == []
    assert String('\n').splitlines() == ['']

def test_linhas():
    assert String('abc\ndef\n').linhas() == ['abc', 'def']
    assert String('').linhas() == []
    assert String('\n').linhas() == []

def test_vazia():
    assert String('').vazia() == True
    assert String('   \n').vazia() == True
    assert String('.').vazia() == False
    
def test_length():
    s = String("abc")
    assert len(s) == 3
    s.trocar('b', 'abc')
    assert len(s) == 5
    
def test_add():
    s = String('abc')
    assert s.add('def') == 'abcdef'
    s.add('ghi', len(s)-3)
    assert s == 'abcghidef'

def test_mask():
    assert String('05/01/1986').mask("##/##/####") == '05/01/1986'
    assert String('06742776609').mask("###.###.###-##") == '067.427.766-09'

def test_parse():
    s = String('50')
    s.val = '60'
    assert int(s) == 60
    assert float(s) == 60.0
