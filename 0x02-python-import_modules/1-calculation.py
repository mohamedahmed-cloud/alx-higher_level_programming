#!/usr/bin/python3

if __name__ == "__main__":
    '''
        import calc function then use it to make clac on them	.
    '''
    from calculator_1 import add, sub, mul, div
    a = 1
    b = 2
    print("{:} + {:} = {:}".format(a, b, add(a  b)))
    print("{:} + {:} = {:}".format(a, b, sub(a + b)))
    print("{:} + {:} = {:}".format(a, b, mul(a + b)))
    print("{:} + {:} = {:}".format(a, b, mul(a + b)))
