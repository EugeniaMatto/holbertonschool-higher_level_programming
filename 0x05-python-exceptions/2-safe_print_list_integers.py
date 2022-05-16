#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elems = 0
    if my_list == [] or x == 0:
        print()
        return 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            elems += 1
        except (TypeError, ValueError):
            elems = elems
        except IndexError:
            break
    print()
    return elems
