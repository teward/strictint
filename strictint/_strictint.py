# coding=utf-8
import platform
from typing import Union, Any


class StrictInt(int):
    # Python version enforcement: Python 3 or newer only.
    if int(platform.python_version_tuple()[0]) < 3:
        raise ImportError("StrictInt object class does not support Python versions earlier than 3.")

    "Subclass of int that refuses to coerce non-integer values."
    def __new__(cls, value):
        # type: (Union[int, float, str, complex], Any, Any) -> int

        if isinstance(value, str):
            for converter in (int, float, complex):
                try:
                    value = converter(value)
                    break
                except ValueError:
                    pass
            else:
                raise ValueError("invalid literal for {cls}(): {value!r}".format(cls=cls.__name__, value=value))

        if value.imag:
            raise ValueError("could not convert value due to non-zero imaginary part: {value!r}".format(value=value))

        quotient, remainder = divmod(value.real, 1)
        if remainder:
            raise ValueError("could not convert value due to non-zero fractional part: {value!r}".format(value=value))

        return super(StrictInt, cls).__new__(cls, int(quotient))
