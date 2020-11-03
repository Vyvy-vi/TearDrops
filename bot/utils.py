import os

sentinel = object()


def get_environment_variable(key, default=sentinel, coerce=str):
    try:
        value = os.environ[key]
        return coerce(value)
    except KeyError:
        if default != sentinel:
            return default
        raise ValueError("You must specify '{}' environment variable.".format(key))
    except Exception as e:
        raise ValueError("Error while parsing environment variable '{}', more info: '{}'.".format(key, e))
