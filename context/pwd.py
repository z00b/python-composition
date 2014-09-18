from contextlib import contextmanager
import os

def print_location(message):
    print 'in directory [{d}]: {m}'.format(d=os.getcwd(), m=message)

@contextmanager
def pwd(directory):
    try:
        cwd = os.getcwd()
        os.chdir(directory)
        yield cwd
    finally:
        os.chdir(cwd)

def main():
    print_location('pre-context')
    with pwd('/') as previous:
        print previous
        print_location('in context')
    print_location('post-context')

if __name__ == '__main__':
    main()
