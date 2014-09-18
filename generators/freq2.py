# Slight change from freq1.py, leveraging the default value
# in `dictionary.get` to remove the clutter of the if/else
# clause.

from pprint import pprint
import sys

def count_words(f):
    counts = {}
    lines = f.readlines()
    for line in lines:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1
    return counts

def main():
    filename = sys.argv[1]
    with open(filename) as infile:
        frequencies = count_words(infile)
        pprint(frequencies)

if __name__ == '__main__':
    main()
