#!/usr/bin/python
"""Linked List Module"""


class Node:
    """class Node"""

    def __init__(self, data, next_node=None):
        """Initialize"""
        if type(data) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = data
        if type(next_node) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node

    @property
    def data(self):
        """Get data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Get next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next_node"""
        if type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """class Singly Linked List"""

    def __init__(self):
        """Initalize"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert node in ascendant order"""
        current = self.__head

        if current is None or current.data > value:
            self.__head = Node(value, self.__head)
        else:
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            current.next_node = Node(value, current.next_node)

    def __str__(self):
        """Print every node"""
        current = self.__head
        str_list = ""

        while current:
            str_list += str(current.data) + '\n'
            current = current.next_node

        return str_list[:-1]
