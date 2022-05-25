Import function:

>>> add_integer = __import__('0-add_integer').add_integer

Test function:

>>> add_integer(5, 7)
12

>>> add_integer(7)
105

>>> add_integer(True, False)
Traceback (most recent call last):
TypeError: a must be an integer

>>> add_integer(3,'ola')
Traceback (most recent call last):
TypeError: b must be an integer

>>> add_integer(0.3342, 0.922139)
0

>>> add_integer(9223372036854775808, 1)
9223372036854775809

>>> add_integer(98, None)
Traceback (most recent call last):
TypeError: b must be an integer

>>> add_integer(3+5j, 3+5j)
Traceback (most recent call last):
TypeError: a must be an integer

>>> add_integer(1000e1000, 1000e1000)
Traceback (most recent call last):
OverflowError: cannot convert float infinity to integer

>>> add_integer(10e10, -10e10)
0

>>> add_integer(-40, -240)
-280

>>> add_integer("hola")
Traceback (most recent call last):
TypeError: a must be an integer
