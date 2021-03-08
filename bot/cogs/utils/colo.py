import random

class COLOR:
    DEFAULT = 0x8FDDE7
    ERROR = 0xFF3333
    SUCCESS = 0xB6E5D8
    READY = 0xB6E5D8
    SADNESS = 0x0f0f18
    JOY = 0xFBE5C8
    LEVELLING = 0xFFC2C7
    ECONOMY = 0x85bb65
    WIKI = 0xa9a9aa
    XKCD = 0x96a8c8
    COFFEE = 0x8c4e08

    @staticmethod
    def RANDOM() -> int:
        color = "%06x" % random.randint(0, 0xFFFFFF)
        return int(color, 16)
