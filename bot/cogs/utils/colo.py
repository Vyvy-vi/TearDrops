import random


class COLOR:
    DEFAULT = 0x8FDDE7
    ERROR = 0xFF3333
    SUCCESS = 0xB6E5D8
    READY = 0xB6E5D8
    SADNESS = 0x0F0F18
    JOY = 0xFBE5C8
    LEVELLING = 0xFFC2C7
    ECONOMY = 0x85BB65
    WIKI = 0xA9A9AA
    XKCD = 0x96A8C8
    COFFEE = 0x8C4E08

    @staticmethod
    def RANDOM() -> int:
        return int(hex(random.randint(0, 0xFFFFFF)), 16)
