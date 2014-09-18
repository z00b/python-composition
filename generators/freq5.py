# Same as freq4.py, but converting the list comprehension into
# a generator expression. Now we're back to lazy-evaluation and
# memory is happy again.

from pprint import pprint
import sys

def count_words(f):
    counts = {}
    for word in (w for l in f for w in l.split()):
        counts[word] = counts.get(word, 0) + 1
    return counts

def main():
    filename = sys.argv[1]
    with open(filename) as infile:
        frequencies = count_words(infile)
        pprint(frequencies)

if __name__ == '__main__':
    main()
