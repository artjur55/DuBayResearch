import numpy as np

from config_parser import get_config
from type_checker import is_int, is_float, is_bool


def init_lattice(height=10, width=10, meta_ratio=1.0, rand_init=False):
    if meta_ratio == 1.0:
        return -np.ones((height, width), dtype=int)
    if meta_ratio == 0.0:
        return np.ones((height, width), dtype=int)
    num_n_ones = meta_ratio * height * width
    if not rand_init:
        lattice = np.ones((height, width), dtype=int)
        col = -np.ones(height, dtype=int)
        n_cols = int(num_n_ones // height)
        for x in range(0, n_cols):
            lattice[:, x] = col
        for y in range(0, int(num_n_ones % height)):
            lattice[y, n_cols] = -1
        return lattice
    lattice = np.random.choice([-1, 1], size=(height, width), p=[meta_ratio, 1-meta_ratio])
    return lattice


def init_lattice_config():
    conf = get_config(section='Lattice')
    return init_lattice(is_int(conf['height']), is_int(conf['width']),
                        is_float(conf['meta_ratio']), is_bool(conf['rand_init']))
