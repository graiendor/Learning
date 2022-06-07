from xml.etree.ElementTree import tostring


class LinkedList:
    class Node:
        def __init__(self, previous=None, value=None, next=None):
            self.previous = previous
            self.value = value
            self.next = next
    
    def __init__(self):
        self.top = None

    def insert(self, value):
        if self.top is None:
            self.top = self.Node(value=value)
        else:
            node = self.top
            while node.next is not None:
                previous = node
                node = node.next
            node.next = self.Node(value=value)
            node.previous = previous

    def __repr__(self):
        return " ".join([str(item) for item in self.__print__()])

    def __str__(self):
        return " ".join([str(item) for item in self.__print__()])

    def __print__(self) -> str:
        node = self.top
        output = []
        while node != None:
            output.append(node.value)
            node = node.next
        return output
