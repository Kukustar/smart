from typing import List


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def is_empty(self) -> bool:
        return self.head is None

    def return_all_nodes(self) -> List[int]:
        nodes = []
        node = self.head
        while node is not None:
            nodes.append(node.value)
            node = node.next
        return nodes

    def clean(self):
        if self.is_empty():
            return
        self.head = None
        self.tail = None

    def delete(self, val: int, all=False):
        if self.is_empty():
            return
        node = self.head
        prev = None
        while node is not None:
            if node.value == val:
                if prev is None:
                    self.head = node.next
                    if self.head is None:
                        self.tail = None
                    if not all:
                        return
                    else:
                        prev.next = node.next
                        if node.next is None:
                            self.tail = prev
                        if not all:
                            return
                        else:
                            prev = node
            node = node.next

        if all and prev is not None:  # Обновление self.tail для списка, содержащего узлы
            self.tail = prev

    def find_all(self, val: int) -> List[Node]:
        nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                nodes.append(node)
            node = node.next
        return nodes

    def len(self) -> int:
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length

    def insert(self, afterNode: Node, newNode: Node):
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            if self.tail is None:
                self.tail = newNode
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode
            if afterNode == self.tail:
                self.tail = newNode


def sum_linked_lists(list1, list2):
    if list1.len() != list2.len():
        return 

    result_list = LinkedList()
    current1 = list1.head
    current2 = list2.head

    while current1 is not None and current2 is not None:
        sum_value = current1.value + current2.value
        result_list.add_in_tail(Node(sum_value))
        current1 = current1.next
        current2 = current2.next

    return result_list
