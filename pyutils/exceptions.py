from typing import Callable, TypeVar
from contextlib import suppress


_T = TypeVar("_T")

# Expected to be used as a 'with' statement, to suppress any possible exception.
care = suppress(BaseException)


def maybe(function: Callable[[], _T]) -> _T | None:
    """ Evaluates the given function in a safe manner, supressing any possible exception.\n"""
    """ If no exception occurs, the function's output is returned. Otherwise, None is returned."""
    try:
        return function()
    except Exception:
        return None
