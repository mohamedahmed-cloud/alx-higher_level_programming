#!/usr/bin/python3
"""Implementation of Singly Linked List"""


class Node:
    """Node Class is Main Part of Singly Linked list Code"""
    def __init__(self, data, next_node=None):
        """
        Init method like a constructor
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter Method for data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Setter Method for data"""
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Getter Method for next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter Method for next node"""
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Singly Linked List Class"""
    def __str__(self):
        """Method to print the Singly linked list when call the object"""
        res = ""
        head = self.__head
        while head:
            res += str(head.data)
            head = head.next_node
            res += "\n" if head else ""
        # print(head)
        return res

    def __init__(self):
        """Init method, like a constructor"""
        self.__head = None

    def sorted_insert(self, value):
        """Method to insert in singly linked list by a sorted way"""
        head = self.__head
        if self.__head is None:
            self.__head = Node(value)
        else:
            previousNode = None
            newNode = Node(value)

            while head and value > head.data:
                previousNode = head
                head = head.next_node

            newNode.next_node = head
            if previousNode:
                previousNode.next_node = newNode
            else:
                self.__head = newNode
