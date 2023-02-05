from pyutils.exceptions import maybe, care


def test_maybe():
    x = maybe(lambda: 1 / 0) or 1
    assert x == 1
    x = maybe(lambda: 1 / 2) or 1
    assert x == 0.5
    # x = maybe(1)
    # assert x is None


def test_care():
    x = 1
    with care: x = x / 0
    assert x == 1
    with care: x = x * 0
    assert x == 0
