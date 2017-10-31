import Lattice
from init_lattice import init_lattice, init_lattice_config


def main():
    # l = init_lattice()
    # print(l)
    # l = init_lattice(10, 10, 1.0)
    # print(l)
    # l = init_lattice(10, 10, 0.0)
    # print(l)
    # l = init_lattice(10, 10, 0.5)
    # print(l)
    # l = init_lattice(10, 10, 0.99)
    # print(l)
    # l = init_lattice_config()
    # print(l)
    l = Lattice.Lattice()
    print(l.get_state)
    print(l.check_state())


if __name__ == "__main__": main()
