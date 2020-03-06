#!/usr/bin/python3

"""Our own little animal farm."""

import sys

from animals import lion
from animals import cat

def add_animal(farm,animal):
    farm.add(animal)
    return farm

def main(animals):
    farm = set()
    for animal in animals:
        farm = add_animal(farm,animal)
    print("We've got some animals on the farm:", ', '.join(farm) + '.')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Pass at least one animal type!')
        sys.exit(1)
    main(sys.argv[1:])

    if kind == 'cat':
        return cat.Cat()
    if kind == 'lion':
        return lion.Lion()
