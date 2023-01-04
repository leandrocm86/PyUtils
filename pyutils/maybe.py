def maybe(function):
    """ Evaluates the given function in a safe manner, supressing any possible exception.\n"""
    """ If no exception occurs, the function's output is returned. Otherwise, None is returned."""
    try:
        return function()
    except:
        return None
