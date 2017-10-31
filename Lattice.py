from init_lattice import init_lattice_config
from type_checker import is_array


class Lattice:

    def __init__(self, init=None):
        if init:
            self._state = init
        else:
            print(init_lattice_config())
            self._state = init_lattice_config()

    @property
    def get_state(self):
        return self._state

    def check_state(self):
        try:
            self._state = is_array(self._state)
            return True
        except ValueError:
            return False
