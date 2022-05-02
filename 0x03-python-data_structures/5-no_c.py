#!/usr/bin/env python3
def no_c(my_string):
    for i in range(len(my_string)):
        if (my_string[i:i+1] == 'C') or (my_string[i:i+1] == 'c'):
            my_string = my_string[:i] + my_string[i + 1:]
            i = 0
    return my_string
