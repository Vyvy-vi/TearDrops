import random

JOE_WORDS = ["right", "awesome", "interesting", "cool", "cool"]


def joe_generate(lim: int = 4):
    word = ""
    for _ in range(lim):
        rand_word = random.choice(JOE_WORDS)
        word += rand_word.title()
    return word


if __name__ == "__main__":
    print(joe_generate(random.randint(3, 11)))
