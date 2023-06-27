#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        """Defines a node of the linked list"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data getter function"""
        return self.__data

    @data.setter
    def data(self, value):
        """data setter function"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """next_node getter function"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter function"""
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """Defines a singly linked list class"""
        self.__head = None

    def sorted_insert(self, value):
        n = Node(value)
        t = self.__head
        add_start = False

        if not self.__head:
            self.__head = n
            n.next_node = None
        else:
            if value < self.__head.data:
                add_start = True
            while t.next_node and value > t.next_node.data\
                    and not add_start:
                t = t.next_node
            if not add_start:
                    n.next_node = t.next_node
                    t.next_node = n
            else:
                n.next_node = t
                self.__head = n
            n.data = value

    def __str__(self):
        i = ""
        cur = self.__head

        while cur:
            i += str(cur.data) + '\n'
            cur = cur.next_node
        return i[: -1]
