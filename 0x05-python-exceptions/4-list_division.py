#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = my_list_1.copy()
    if (len(my_list_1) < len(my_list_2)):
        new = my_list_2.copy()
    for i in range(list_length):
        res = 0
        try:
            res = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
        except (TypeError, ValueError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            new[i] = res
    return new


