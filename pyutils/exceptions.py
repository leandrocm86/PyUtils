from typing import Callable, TypeVar


_T = TypeVar("_T")


def maybe(function: Callable[[], _T]) -> _T | None:
    """ Evaluates the given function in a safe manner, supressing any possible exception.\n"""
    """ If no exception occurs, the function's output is returned. Otherwise, None is returned."""
    try:
        return function()
    except Exception:
        return None


# ABANDONADO PORQUE INTERROMPE NULL_SAFE NA CHECAGEM DE TIPO.
# MELHOR USAR MAYBE COM OPERADOR 'OR'
# class default():
#     """ Initializes a variable with a default value to be used if the following expression raises an exception.\n"""
#     """ Expected to be used as a 'with' statement, to suppress any possible exception.\n"""
#     """ Example: with default(0) as x: x = 10/y """
#     def __init__(self, default):
#         self.default = default
#     def __enter__(self):
#         return self.default
#     def __exit__(self, type, value, traceback):
#         return True
