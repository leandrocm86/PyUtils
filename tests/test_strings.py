from pyutils.strings import String


def test_line_with():
    text = String('abaxi ácido\nbanana doce\nlaranja doce\nmorango bom')
    assert text.line_with('banana') == 'banana doce'
    assert text.line_with('banana', 'doce') == 'banana doce'
    assert text.line_with('abacate') == None


def test_lines_with():
    text = String('abaxi ácido\nbanana doce\nlaranja doce\nmorango bom')
    assert text.lines_with('doce') == ['banana doce', 'laranja doce']
    assert text.lines_with('azedo') == []


def test_cell_with():
    text = String('↳ Corsair Corsair STRAFE Gaming Keyboard Consumer Control   id=19   [slave  keyboard (3)]')
    assert text.cell_with('id=') == 'id=19'


def test_starting_after():
    text = String('AAAabcZZZdefAAAglAAAmAAApqr')
    assert text.startingafter('AAA', 3) == 'mAAApqr'


def test_starting_ending():
    text = String('↳ Corsair Corsair STRAFE Gaming Keyboard Consumer Control   id=19   [slave  keyboard (3)]')
    assert text.startingafter('id=').endingbefore(' ') == '19'
    assert text.startingwith('[').endingwith(']') == '[slave  keyboard (3)]'
    assert text.startingwith('STRAFE').endingbefore('Control') == 'STRAFE Gaming Keyboard Consumer '
    text = String('abc1def1abc2def2abc3def3')
    assert text.startingwith('abc', 2).endingbefore('def', 2) == 'abc2def2abc3'


def test_startingafterlast_endingwithlast():
    s = String('/home/l86/scripts/teste.py')
    assert s.startingafter('/', s.count('/')) == 'teste.py'
    assert s.endingwith('/', s.count('/')) == '/home/l86/scripts/'


def test_strip():
    original = String(' teste123\n')
    change = original.strip()
    assert original == ' teste123\n'
    assert change == 'teste123'


def test_trim():
    mutavel = String(' teste123\n')
    mutavel.trim()
    assert mutavel.val == 'teste123'


def test_replace():
    original = String('abacaxi')
    change = original.replace('a', 'e')
    assert original == 'abacaxi'
    assert change == 'ebecexi'


def test_change():
    mutavel = String('abacaxi')
    mutavel.change('a', 'e')
    assert mutavel == 'ebecexi'


def test_strtodate():
    date = String.strtodate('05/01/1986')
    assert date.year == 1986
    assert date.month == 1
    assert date.day == 5


def test_todate():
    date = String('05/01/1986 13:30').todate('%d/%m/%Y %H:%M')
    assert date.year == 1986
    assert date.month == 1
    assert date.day == 5
    assert date.hour == 13
    assert date.minute == 30


def test_fromdate():
    date = String('05/01/1986 13:30:59').todate('%d/%m/%Y %H:%M:%S')
    assert String.fromdate(date, '%d-%m-%Y %H:%M') == '05-01-1986 13:30'
    date = String.strtodate('31/12/2000')
    assert String.fromdate(date, '%d-%m-%Y - %H:%M') == '31-12-2000 - 00:00'


def test_fromdate_now():
    s1 = String.fromdate(format='%H:%M:%S')
    assert len(s1) == 8 and s1 != '00:00:00'
    s2 = String.fromdate(format='%H:%M:%S,%f')
    assert len(s2) == 15 and s2 != '00:00:00.000000'
    s3 = String.fromdate(format='%d/%m/%Y')
    assert len(s3) == 10 and s3 != '01/01/1970'
    s4 = String.fromdate(format='%d/%m/%Y %H:%M:%S')
    assert len(s4) == 19 and s4 != '01/01/1970 00:00:00'


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


def test_lines():
    assert String('abc\ndef\n').lines() == ['abc', 'def']
    assert String('').lines() == []
    assert String('\n').lines() == []


def test_empty():
    assert String('').empty() == True
    assert String('   \n').empty() == True
    assert String('.').empty() == False


def test_length():
    s = String("abc")
    assert len(s) == 3
    s.change('b', 'abc')
    assert len(s) == 5


def test_add():
    s = String('abc')
    assert s.add('def') == 'abcdef'
    s.add('ghi', -3)
    assert s == 'abcghidef'


def test_mask():
    assert String('05/01/1986').mask("##/##/####") == '05/01/1986'
    assert String('06742776609').mask("###.###.###-##") == '067.427.766-09'


def test_parse():
    s = String('50')
    s.val = '60'
    assert int(s) == 60
    assert float(s) == 60.0


def test_get():
    s = String('abcd')
    s = s[:-1]
    assert s == 'abc' and isinstance(s, String)


def test_contains_all_contains_any():
    text = String('abcdefghijklmnopqrs')
    assert text.contains_all('abc', 'jkl', 'qrs')
    assert not text.contains_all('abc', 'jkl', 'xyz')
    assert text.contains_any('abc', 'jkl', 'xyz')
    assert not text.contains_any('uvw', 'xyz')

