def wrapper(fn):
    def inner():
        fn()
        fn()
        return fn()
    return inner

def myfun():
    print 'hello'

wrapped = wrapper(myfun)
print 'about to call wrapped'
wrapped()
