import configparser as cp

c = cp.ConfigParser()
c.read('config.ini')


def get_config(section=None):
    if section:
        return to_dict(section)

    full_dict = {}
    for s in c.sections():
        full_dict[s] = to_dict(s)


def to_dict(section):
    parsed_dict = {}
    for o in c.options(section):
        parsed_dict[o] = c.get(section, o)
    return parsed_dict
