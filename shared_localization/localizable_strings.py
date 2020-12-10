from yaml import safe_load


def load_localizable_strings_from_yaml(yaml):
    return safe_load(yaml)
