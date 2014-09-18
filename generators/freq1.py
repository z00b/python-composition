# The "brute force" first-pass method, being as verbose as possible

from pprint import pprint
import sys

def count_words(f):
    counts = {}
    lines = f.readlines()
    for line in lines:
        words = line.split()
        for word in words:
            if word in counts:
                counts[word] = counts[word] + 1
            else:
                counts[word] = 1
    return counts

def main():
    filename = sys.argv[1]
    with open(filename) as infile:
        frequencies = count_words(infile)
        pprint(frequencies)

if __name__ == '__main__':
    main()
