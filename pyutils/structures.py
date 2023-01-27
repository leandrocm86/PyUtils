from collections.abc import Iterator
from typing import Callable, TypeVar, Any

_T = TypeVar("_T")


class Lists:

    @staticmethod
    def __to_float(x):
        if isinstance(x, float) or isinstance(x, int) or isinstance(x, str):
            return float(x)
        raise Exception(f'Object of type {type} cannot be converted to float.')

    @staticmethod
    def average(listable: Iterator[_T] | list[_T], function: Callable[[_T], float] = __to_float, default=0.0) -> float:
        """ Returns the average of a list. If it's empty, a default value is returned.\n
            An optional function may be specified to extract the value for each item in the list.\n
            By default, the value for each item is the item itself (an error will be thrown if it's not convertible to float). """
        listable = list(listable)
        if not listable:
            return default
        from statistics import fmean
        return fmean([function(x) for x in listable])

    @staticmethod
    def groupby(list: list[_T], keyfunction: Callable[[_T], Any], ignore_nones=True) -> dict:
        """ Similar to more_itertools.map_reduce, grouping items from a list into a dict.\n
            They are different from itertools.groupby because don't need to be sorted beforehand,\n
            and also because they return a whole dict instead of iterators. """
        output = {}
        for e in list:
            key = keyfunction(e)
            if key is not None or not ignore_nones:
                output.setdefault(key, []).append(e)
        return output

    @staticmethod
    def get(list: list, index: int, default=None):
        """ Returns the element at the given index of a list.\n
        If it's out of bounds, or if it evaluates to false, a default value is returned. """
        try:
            return list[index] if list[index] else default
        except IndexError:
            return default

    @staticmethod
    def print(list: list[_T], header='', elem_to_string: Callable[[_T], str] = lambda e: str(e), separator=', '):
        print(header + separator.join([elem_to_string(e) for e in list]))


class Dicts:

    @staticmethod
    def put_if_value(dictionary: dict, key, value):
        """ Put the value in the dictionary if it is not None or empty. """
        if value:
            dictionary[key] = value

    @staticmethod
    def append(dictionary: dict, key, value):
        """ For use in dict of lists.\n
        Append the value to a list in the dictionary.\n
        Instantiates the list when the first value is being appended. """
        dictionary.setdefault(key, []).append(value)
