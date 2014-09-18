# Stop calling `.readlines()` on the file because files
# are iterable in Python, returning one line at a time
# Saves loading the whole thing into memory

from pprint import pprint
import sys

def count_words(f):
    counts = {}
    for line in f:
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
