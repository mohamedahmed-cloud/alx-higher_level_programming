#!/usr/bin/python3

if __name__ == "__main__":
    '''
        import add function then use it to add to number.
    '''
    from add_0 import add
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a + b)))
