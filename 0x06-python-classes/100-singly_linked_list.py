#!/usr/bin/python3
"""
A class Node that defines a node of a singly linked list by:
(a) Private instance attribute, data
(b) Private instance attribute, next_node
(c) Instantiation with data and next_node
"""


class Node():
    """
    The Node class
    """

    def __init__(self, data, next_node=None):
        """
        Initize the class using a constructor
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Private instance attribute: Data
        """
        return self.__data

    @data.setter
    def data(self, DataValue):
        """
        Setting the private instance attribute data
        """
        if type(DataValue) != int:
            raise TypeError("data must be an integer")
        self.__data = DataValue

    @property
    def next_node(self):
        """
        The node

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, NodeValue):
        """
        settting the node"""
        if NodeValue is not None and not isinstance(NodeValue, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = NodeValue


class SinglyLinkedList():
    """
    Now, let us create the class SinglyLinkedList
    """
    def __init__(self):
        """
        Let us initialize the SinglyLinkedList class using a constructor
        """
        self.__head = None

    def sorted_insert(self, DataValue):
        """
        Let us then inserts the  node
        """
        NewNode = Node(DataValue)
        if self.__head is None:
            self.__head = NewNode
            return
        if DataValue < self.__head.data:
            NewNode.next_node = self.__head
            self.__head = NewNode
            return
        actual = self.__head
        while DataValue >= actual.data:
            prev = actual
            if actual.next_node:
                actual = actual.next_node
            else:
                actual.next_node = NewNode
                return
        prev.next_node = NewNode
        NewNode.next_node = actual

    def __str__(self):
        strg = ""
        actual = self.__head
        while actual:
            strg += str(actual.data) + "\n"
            actual = actual.next_node
        return strg[:-1]
