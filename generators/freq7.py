# An example of a purely declarative style
# Sometimes this approach is awesome. In this case, it's awful.
# Calling `sorted` on the generator forces it to be fully realized
# (and copied!) so memory usage explodes.

from itertools import groupby
from pprint import pprint
import sys

def wordgen(f):
    for line in f:
        for word in line.split():
            yield word

def count_words(f):
    ordered = sorted(wordgen(f))
    groups = groupby(ordered)
    counts = ((k, len(list(v))) for k,v in groups)
    return dict(counts)

def main():
    filename = sys.argv[1]
    with open(filename) as infile:
        frequencies = count_words(infile)
        pprint(frequencies)

if __name__ == '__main__':
    main()
