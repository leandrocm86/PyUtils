from pyutils.lists import average, groupby, printlist, flat, compare


def test_average():
    assert average([1, 2, 3]) == 2
    assert average([]) == 0
    assert average(i for i in range(11)) == 5
    assert average(i for i in range(3) if i > 3) == 0
    assert average(['a', 'ab', 'abc'], lambda s: len(s)) == 2


def test_groupby():
    test_list: list[int] = []
    test_list.append(1); test_list.append(2); test_list.append(3)
    result = groupby(test_list, lambda x: x % 2)
    assert result == {1: [1, 3], 0: [2]}
    result = groupby(test_list, lambda x: str(x) if x < 3 else None)
    assert result == {'1': [1], '2': [2]}


def test_lists_print(capfd):  # capfd is a fixture to capture stdout and stderr
    printlist(['abc', 'def', 'ghi'], 'Print Test: ')
    assert capfd.readouterr().out == 'Print Test: abc, def, ghi\n'


def test_flat():
    assert flat([1, 2, 3]) == [1, 2, 3]
    assert flat([]) == []
    assert flat([1, 2, [3, 4]]) == [1, 2, 3, 4]
    assert flat([[1], 2, [3, 4]]) == [1, 2, 3, 4]
    assert flat([[1, [2]], [3, 4]]) == [1, 2, 3, 4]
    assert flat([[1, [2]], [3, 4]]) == [1, 2, 3, 4]
    assert flat(i for i in range(10) if i % 2 == 0) == [0, 2, 4, 6, 8]
    assert flat([['abc', 'def'], ['ghi']]) == ['abc', 'def', 'ghi']
    assert flat([['abc', None]]) == ['abc', None]


def test_compare():
    assert compare([1, 2, 3, 4, 5, 6], [3, 4, 5, 6, 7, 8]) == ([3, 4, 5, 6], [1, 2], [7, 8])
