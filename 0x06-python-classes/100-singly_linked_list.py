#!/usr/bin/python3
"""Node Class"""


class Node:
    """Define Node"""

    def __init__(self, data, next_node=None):
        """ Init Node """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Get data"""
        return self.__data

    @data.setter
    def data(self, value):
        """ Set data"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter position"""
        if (type(value) != Node and value != None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Define Class"""

    def __init__(self):
        """init function"""
        self.__head = None

    def sorted_insert(self, value):
        if (self.__head == None):
            self.__head = Node(value)
        else:
            a = self.__head
            aux = Node(value)
            ant = None
            while (a != None):
                if (a.data > aux.data):
                    aux.next_node = a
                    if ant:
                        ant.next_node = aux
                    if self.__head == a:
                        self.__head = aux
                    return
                ant = a
                a = a.next_node
            ant.next_node = aux
            aux.next_node = None

    def __str__(self):
        """override str"""
        a = self.__head
        while(a.next_node != None):
            print(a.data)
            a = a.next_node
        print(a.data, end="")
        return ""

