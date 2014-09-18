# Turned the generator expression from freq5 into an actual generator because
# (a) shows how to do it, and
# (b) arguably easier to read, digest, debug, etc
# Definitely a matter of opinion so do what feels right to you

from pprint import pprint
import sys

def wordgen(f):
    for line in f:
        for word in line.split():
            yield word

def count_words(f):
    counts = {}
    for word in wordgen(f):
        counts[word] = counts.get(word, 0) + 1
    return counts

def main():
    filename = sys.argv[1]
    with open(filename) as infile:
        frequencies = count_words(infile)
        pprint(frequencies)

if __name__ == '__main__':
    main()
