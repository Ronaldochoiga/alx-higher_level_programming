#!/usr/bin/python3
"""Defines the classes Node and SinglyLinkedList"""


class Node:
    """
    Class that defines properties Node.

    Attributes:
        data: data field
    """
    def __init__(self, data, next_node=None):
        """Creates new node

        Args:
            __data : data field
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data

        Returns: the data field
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Propery setter

        Args:
            value: data field

        Raises:
            TypeError: data should be integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrives the node

        Returns: The next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Property setter

        Args:
            value: next node.

        Raises:
            TypeError: next_node should be obj
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Class that defines properties linked list

    Attributes:
        head: head of linked list
    """
    def __init__(self):
        """Creates new instance of linked list

        Args:
            __head : head of LinkedList .
        """
        self.__head = None

    def __str__(self):
        """Represents the class obj as strg

        Returns: The class object rep as strg
        """
        tmp = self.__head
        pnode = []
        while tmp:
            pnode.sort()
            pnode.append(str(tmp.data))
            tmp = tmp.next_node

        pnode.sort(key=int)
        return ("\n".join(pnode))

    def sorted_insert(self, value):
        """Inserts a new node at specific pos

        Args:
            value: val
        """
        if self.__head is None:
            nnode = Node(value)
            nnode.next_node = self.__head
            self.__head = nnode
        else:
            nnode = Node(value)
            nnode.data = value
            nnode.next_node = self.__head
            self.__head = nnode
