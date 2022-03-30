import strings as s

def test_linha_com():
    texto = s.String('abaxi ácido\nbanana doce\nlaranja doce\nmorango bom')
    assert texto.linha_com('banana') == 'banana doce'
    assert texto.linha_com('banana', 'doce') == 'banana doce'
    assert texto.linha_com('abacate') == None

def test_linhas_com():
    texto = s.String('abaxi ácido\nbanana doce\nlaranja doce\nmorango bom')
    assert texto.linhas_com('doce') == ['banana doce', 'laranja doce']
    assert texto.linhas_com('azedo') == []

def test_celula_com():
    texto = s.String('↳ Corsair Corsair STRAFE Gaming Keyboard Consumer Control   id=19   [slave  keyboard (3)]')
    assert texto.celula_com('id=') == 'id=19'

def test_desde_ate():
    texto = s.String('↳ Corsair Corsair STRAFE Gaming Keyboard Consumer Control   id=19   [slave  keyboard (3)]')
    assert texto.desde('id=').ate(' ') == '19'
