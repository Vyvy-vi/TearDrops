import math
import random

creatures = "cat doggo parrot parakeet turtle mouse squirell elephant lion dog hamster walrus seal fish shark clam coral whale crab lobster starfish eel dolphin squid jellyfish ray shrimp mantaRay angler snorkler scubaDiver urchin anemone morel axolotl".split(" ")
objects = "boat ship submarine car yacht dinghy raft kelp seaweed anchor".split(" ")
adjective_descriptors = "cute adorable lovable happy sandy bubbly friendly floating drifting floofy cwute fluffy".split(" ")
size_descriptors = "large big small giant massive tiny little huge".split(" ")
creature_descriptors = "sleeping eating jumping yeeting lurking crying hiding sobbing".split(" ")

nlist = creatures + objects
descriptors = adjective_descriptors + size_descriptors

colors = "blue blueGreen darkCyan electricBlue greenBlue lightCyan lightSeaGreen seaGreen turquoise aqua aquamarine teal cyan gray darkBlue cerulean azure lapis navy red yellow pink violet purple".split(" ")

rand = lambda array: array[math.floor(random.random()*len(array))]

random_noun = lambda: rand(nlist)
random_descriptor = lambda noun: rand(descriptors) if noun not in creatures else rand(descriptors + creature_descriptors)
random_color = lambda: rand(colors)
format = lambda array: "".join(map(lambda word: word.title(), array))

def generate(max_size:int = 30):
  noun = random_noun()
  descriptor = random_descriptor(noun)
  color = random_color()

  if len(descriptor + noun + color) <= max_size:
    return format([descriptor, color, noun])
  elif len(descriptor + noun) <= max_size:
    return format([descriptor, color])
  elif len(color + noun) <= max_size:
    return format([color, noun])
  else:
    return format([noun])[:max_size]

if __name__ == "__main__":
    print(generate(random.randint(5,30)))
