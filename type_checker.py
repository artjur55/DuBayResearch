import numpy as np


def is_int(s):
    try:
        i = int(s)
        return i
    except ValueError:
        raise(s + " is not an integer.")


def is_float(s):
    try:
        f = float(s)
        return f
    except ValueError:
        raise (s + " is not a float.")


def is_bool(s):
    if s == 'True':
        return True
    if s == 'False':
        return False
    raise ValueError(s + " is not an boolean.")


def is_array(s):
    if type(s) is np.ndarray:
        return s
    raise ValueError("The following value in not an array:\n" + s)
