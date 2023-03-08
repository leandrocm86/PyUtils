from typing import Callable, Generator, Generic, Iterable, Tuple, TypeVar, Any

from pyparsing import anyOpenTag

_T = TypeVar('_T')


def __to_float(x):
    if isinstance(x, float) or isinstance(x, int) or isinstance(x, str):
        return float(x)
    raise Exception(f'Object of type {type} cannot be converted to float.')


def average(listable: Iterable[_T], function: Callable[[_T], float] = __to_float, default=0.0) -> float:
    """ Returns the average of a list. If it's empty, a default value is returned.\n
        An optional function may be specified to extract the value for each item in the list.\n
        By default, the value for each item is the item itself (an error will be thrown if it's not convertible to float). """
    listable = list(listable)
    if not listable:
        return default
    from statistics import fmean
    return fmean([function(x) for x in listable])


def groupby(list: Iterable[_T], keyfunction: Callable[[_T], Any], ignore_nones=True) -> dict:
    """ Similar to more_itertools.map_reduce, grouping items from a list into a dict.\n
        They are different from itertools.groupby because don't need to be sorted beforehand,\n
        and also because they return a whole dict instead of iterators. """
    output = {}
    for e in list:
        key = keyfunction(e)
        if key is not None or not ignore_nones:
            output.setdefault(key, []).append(e)
    return output


def printlist(list: Iterable[_T], header='', elem_to_string: Callable[[_T], str] = lambda e: str(e), separator=', '):
    print(header + separator.join([elem_to_string(e) for e in list]))


def flat(list_of_lists: Iterable[_T | Iterable[_T] | Iterable[Iterable[_T]]]) -> list[_T]:
    '''
        Flattens n-depth collections (multidimensional arrays), outputing a single regular list with all inner elements.\n
        note: type hints get confused after depth = 3 (list of lists of lists).
    '''
    flatlist = []

    def add(iterable):
        for item in iterable:
            if isinstance(item, Iterable) and not isinstance(item, str): # str is also an Iterable, but we must treat it as an element in this context.
                add(item)
            else:
                flatlist.append(item)

    add(list_of_lists)
    return flatlist
