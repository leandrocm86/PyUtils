from pyutils.exceptions import maybe


def test_maybe():
    x = maybe(lambda: 1 / 0) or 1
    assert x == 1
    x = maybe(lambda: 1 / 2) or 1
    assert x == 0.5
