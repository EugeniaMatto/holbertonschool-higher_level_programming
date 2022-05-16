#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
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
            new.append(res)
    return new
