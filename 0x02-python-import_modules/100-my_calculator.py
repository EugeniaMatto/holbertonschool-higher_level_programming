#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, div, mul, sub
    import sys
    le = len(sys.argv)
    if (le != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if (sys.argv[2] != '+' and sys.argv[2] != '/' and
            sys.argv[2] != '*' and sys.argv[2] != '-'):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if (sys.argv[2] == '+'):
        cuenta = add(int(sys.argv[1]), int(sys.argv[3]))
    if (sys.argv[2] == '-'):
        cuenta = sub(int(sys.argv[1]), int(sys.argv[3]))
    if (sys.argv[2] == '*'):
        cuenta = mul(int(sys.argv[1]), int(sys.argv[3]))
    if (sys.argv[2] == '/'):
        cuenta = div(int(sys.argv[1]), int(sys.argv[3]))
    print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {cuenta:d}")
