import os
import random

sentinel = object()


def get_environment_variable(key, default=sentinel, coerce=str):
    try:
        value = os.environ[key]
        return coerce(value)
    except KeyError:
        if default != sentinel:
            return default
        raise ValueError(
            "You must specify '{}' environment variable.".format(key))
    except Exception as e:
        raise ValueError(
            "Error while parsing environment variable '{}', more info: '{}'.".format(
                key, e))


class COLOR:
    DEFAULT = 0x922C40
    ERROR = 0x922C40
    SUCCESS = 0x922C40
    READY = 0x922C40
    WELCOME = 0x922C40
    SADNESS = 0x922C40
    JOY = 0x922C40
    LEVELLING = 0x922C40
    ECONOMY = 0x922C40
    WIKI = 0x922
    XKCD = 0x922C40

    @staticmethod
    def RANDOM():
        color = "%06x" % random.randint(0, 0xFFFFFF)
        return int(color, 16)
