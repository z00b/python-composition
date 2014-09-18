def adder_maker(num):
    def adder(other):
        return num + other
    return adder

if __name__ == '__main__':
    adderf = adder_maker(1)
    print adderf(2)
