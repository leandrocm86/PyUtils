class Lists:

    @staticmethod
    def average(listable, default=0):
        """ Returns the average of the list. """
        if not listable:
            return default
        if not isinstance(listable, list):
            listable = list(listable)
        return sum(listable) / len(listable)


class Dicts:
    
        @staticmethod
        def put_if_value(dictionary, key, value):
            """ Put the value in the dictionary if it is not None. """
            if value:
                dictionary[key] = value
        
        @staticmethod
        def append(dictionary, key, value):
            """ For use in dict of lists. """ 
            """ Append the value to a list in the dictionary. """
            """ Instantiates the list when the first value is being appended. """
            if key not in dictionary:
                dictionary[key] = []
            dictionary[key].append(value)