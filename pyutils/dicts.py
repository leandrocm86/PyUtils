from typing import Iterable, TypeVar

_K = TypeVar('_K')
_V = TypeVar('_V')


def put_if_value(dictionary: dict[_K, _V], key: _K, value: _V):
    ''' Put the value in the dictionary if it is not None or empty. '''
    if value:
        dictionary[key] = value


def dict_append(dictionary: dict[_K, list[_V]], key: _K, value: _V):
    '''
        For use in multivalue dicts (dict of lists).\n
        Append the value to a list in the dictionary on the given key.\n
        Instantiates the list when the first value is being appended.
    '''
    dictionary.setdefault(key, []).append(value)


def dict_extend(dictionary: dict[_K, list[_V]], key: _K, values: Iterable[_V]):
    '''
        For use in multivalue dicts (dict of lists).\n
        Append all the values to a list in the dictionary on the given key.\n
        Instantiates the list when the first value is being appended.
    '''
    dictionary.setdefault(key, []).extend(values)

