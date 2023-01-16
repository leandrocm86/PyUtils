class Lists:

    @staticmethod
    def average(listable, function=lambda x: x, default=0):
        """ Returns the average of a list. If it's empty, a default value is returned.\n
            An optional function may be specified to extract the value for each item in the list.\n
            By default, the value for each item is the item itself (an error will be thrown if it's not numeric). """
        if not isinstance(listable, list):
            listable = list(listable)
        if not listable:
            return default
        from statistics import fmean
        return fmean([function(x) for x in listable])

    @staticmethod
    def groupby(list, keyfunction, ignore_nones=True) -> dict:
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
    def get(list, index: int, default=None):
        """ Returns the element at the given index of a list.\n
        If it's out of bounds, or if it evaluates to false, a default value is returned. """
        try:
            return list[index] if list[index] else default
        except IndexError:
            return default


class Dicts:
    
    @staticmethod
    def put_if_value(dictionary, key, value):
        """ Put the value in the dictionary if it is not None or empty. """
        if value:
            dictionary[key] = value
    
    @staticmethod
    def append(dictionary, key, value):
        """ For use in dict of lists. """ 
        """ Append the value to a list in the dictionary. """
        """ Instantiates the list when the first value is being appended. """
        dictionary.setdefault(key, []).append(value)