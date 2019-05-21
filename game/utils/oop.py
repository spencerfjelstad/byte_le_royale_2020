# oop file for functions that simulates Object Oriented Programming ideas


def overrides(interface_class):
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider
