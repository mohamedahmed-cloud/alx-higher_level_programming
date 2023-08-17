#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    allowed = "+-*/"
    n -= 1
    print(argv)

    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    print(operator)

    b = int(argv[3])
    if operator not in allowed:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    match operator:
        case "+":
            from calculator_1 import add
            print("{:} + {:} = {:}".format(a, b, add(a, b)))

        case "-":
            from calculator_1 import sub
            print("{:} - {:} = {:}".format(a, b, sub(a, b)))

        case "*":
            from calculator_1 import mul
            print("{:} * {:} = {:}".format(a, b, mul(a, b)))

        case "/":
            from calculator_1 import div
            print("{:} / {:} = {:}".format(a, b, div(a, b)))
