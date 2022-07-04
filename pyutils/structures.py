class Lists:

    @staticmethod
    def average(listable, default=0):
        """ Returns the average of the list. If it's empty, a default value is returned. """
        if not isinstance(listable, list):
            listable = list(listable)
        if not listable:
            return default
        return sum(listable) / len(listable)

    @staticmethod
    def groupby(list, keyfunction, ignore_nones=True) -> dict:
        output = {}
        for e in list:
            key = keyfunction(e)
            if key is not None or not ignore_nones:
                output.setdefault(key, []).append(e)
        return output


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