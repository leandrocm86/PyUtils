from pyutils.structures import Lists, Dicts


def test_average():
    assert Lists.average([1, 2, 3]) == 2
    assert Lists.average([]) == 0
    assert Lists.average(i for i in range(11)) == 5
    assert Lists.average(i for i in range(3) if i > 3) == 0


def test_put_if_value():
    d = {}
    Dicts.put_if_value(d, 'a', 1)
    Dicts.put_if_value(d, 'b', 2)
    Dicts.put_if_value(d, 'c', None)
    assert d == {'a': 1, 'b': 2}


def test_append():
    d = {}
    Dicts.append(d, 'a', 1)
    Dicts.append(d, 'a', 2)
    Dicts.append(d, 'a', 3)
    Dicts.append(d, 'b', 4)
    assert d == {'a': [1, 2, 3], 'b': [4]}