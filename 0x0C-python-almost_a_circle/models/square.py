#!/usr/bin/python3
""" 2º class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ init """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """ getter size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update function """
        le = len(args)
        if (le > 0):
            self.id = args[0]
            if (le > 1):
                self.size = args[1]
            if (le > 2):
                self.x = args[2]
            if (le > 3):
                self.y = args[3]
        else:
            for k, v in kwargs.items():
                if (k == "x"):
                    self.x = v
                if (k == "y"):
                    self.y = v
                if (k == "id"):
                    self.id = v
                if (k == "size"):
                    self.size = v
