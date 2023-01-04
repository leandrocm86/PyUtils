def maybe(function):
    try:
        return function()
    except:
        return None