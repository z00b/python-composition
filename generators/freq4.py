# Compared to freq3.py, moves the double for-loop into a
# list comprehension. This approach is a step backward from
# freq3, because it has to realize the entire list of words,
# including a copy for each time it appears. Memory hog.

from pprint import pprint
import sys

def count_words(f):
    counts = {}
    for word in [w for l in f for w in l.split()]:
        counts[word] = counts.get(word, 0) + 1
    return counts

def main():
    filename = sys.argv[1]
    with open(filename) as infile:
        frequencies = count_words(infile)
        pprint(frequencies)

if __name__ == '__main__':
    main()
