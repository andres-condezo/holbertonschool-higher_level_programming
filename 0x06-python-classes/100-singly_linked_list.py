#!/usr/bin/python3
"""singly linked list module"""


class Node:
    """Node class"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get __data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """set __data attribute"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get __next_node attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set __next_node attribute"""
        if type(value) != Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """SiglyLinkedList class"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        temp = self.__head
        list_nodes = []
        while temp:
            list_nodes.append(str(temp.data))
            temp = temp.next_node
        return "\n".join(list_nodes)

    def sorted_insert(self, value):
        """Public instance method that inserts a new Node into the
           correct sorted position in the list (increasing order)"""
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node

        elif new_node.data <= self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            prev = None

            while current and new_node.data > current.data:
                prev = current
                current = current.next_node

            prev.next_node = new_node
            new_node.next_node = current
