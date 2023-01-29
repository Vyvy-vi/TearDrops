import os
from dotenv import load_dotenv

load_dotenv()

sentinel = object()


def get_environment_variable(key, default=sentinel, coerce=str):
    try:
        value = os.environ[key]
        return coerce(value)
    except KeyError:
        if default != sentinel:
            return default
        raise ValueError(f"You must specify '{key}' environment variable.")
    except Exception as e:
        raise ValueError(
            f"Error while parsing environment variable '{key}', more info: '{e}'."
        )
