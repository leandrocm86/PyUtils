from pyutils.dicts import put_if_value, dict_append


def test_put_if_value():
    d = {}
    put_if_value(d, 'a', 1)
    put_if_value(d, 'b', 2)
    put_if_value(d, 'c', None)
    assert d == {'a': 1, 'b': 2}


def test_append():
    d = {}
    dict_append(d, 'a', 1)
    dict_append(d, 'a', 2)
    dict_append(d, 'a', 3)
    dict_append(d, 'b', 4)
    assert d == {'a': [1, 2, 3], 'b': [4]}
