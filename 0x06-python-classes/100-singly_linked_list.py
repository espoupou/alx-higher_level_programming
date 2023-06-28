#!/usr/bin/python3
"""Module that define a Node class and a singly list.
"""


class Node:
    """class Node that defines a node
    """

    def __init__(self, data, next_node=None):
        """Initialize method that stores the size of the square

        Args:
            data (int): size of the square
            next_node (int, int): square position in space
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = int(data)

        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """int: node data"""
        return self.__data

    @data.setter
    def data(self, value):
        """node data setter
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Node: the next node object"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set the next node
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list
    """

    def __init__(self):
        """init class object
        """
        self.__head = None

    def __str__(self):
        """class string
        """
        node = self.__head
        nodes = ""

        while node is not None:
            nodes += str(node.data)
            if node.next_node is not None:
                nodes += "\n"
            node = node.next_node

        return nodes

    def sorted_insert(self, value):
        """insert new node at the correct place

        Args:
            value (int): new node value
        """
        node = self.__head
        prev = node

        while node is not None:
            if node.data > value:
                break
            prev = node
            node = node.next_node

        newNode = Node(value, node)
        if node == self.__head:
            self.__head = newNode
        else:
            prev.next_node = newNode
