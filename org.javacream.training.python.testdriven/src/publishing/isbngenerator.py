from random import Random
import sys


class IsbnGenerator(object):
    def __init__(self, prefix="ISBN:", suffix="-de"):
        self.generator = Random()
        self.prefix = prefix
        self.suffix = suffix
    def next_isbn(self):
        randomPart = self.generator.randint(0, sys.maxsize)
        return self.suffix + str(randomPart) + self.prefix
         
        