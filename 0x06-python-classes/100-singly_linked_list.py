#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    def __str__(self):
        res = ""
        head = self.__head
        while head:
            res += str(head.data)
            head = head.next_node
            res += "\n" if head else ""
        # print(head)
        return res

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
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
