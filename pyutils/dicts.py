def put_if_value(dictionary: dict, key, value):
    """ Put the value in the dictionary if it is not None or empty. """
    if value:
        dictionary[key] = value


def dict_append(dictionary: dict, key, value):
    """ For use in dict of lists.\n
    Append the value to a list in the dictionary.\n
    Instantiates the list when the first value is being appended. """
    dictionary.setdefault(key, []).append(value)
