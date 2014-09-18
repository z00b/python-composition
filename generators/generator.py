import time
def sillygen():
    time.sleep(2)
    yield 'a'
    time.sleep(2)
    yield 'b'
    time.sleep(2)
    yield 'c'
    time.sleep(2)

def notasillygen():
    l = []
    time.sleep(2)
    l.append('a')
    time.sleep(2)
    l.append('b')
    time.sleep(2)
    l.append('c')
    time.sleep(2)
    return l

print 'a gen'
for i, x in enumerate(sillygen()):
    print i, x

print 'not a gen'
for i, x in enumerate(notasillygen()):
    print i, x
