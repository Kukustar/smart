from typing import List, Optional


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

        if all and prev is not None:
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

    def insert(self, afterNode: Optional[Node], newNode: Node):
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


def test_delete():
    my_list = LinkedList()

    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(20))
    my_list.add_in_tail(Node(30))
    my_list.add_in_tail(Node(20))
    my_list.add_in_tail(Node(30))

    my_list.delete(10)
    assert my_list.return_all_nodes() == [20, 30, 20, 30]
    my_list.delete(20, all=True)
    assert my_list.return_all_nodes() == [30, 30]


def test_clean():
    my_list = LinkedList()

    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(20))
    my_list.add_in_tail(Node(30))
    my_list.add_in_tail(Node(20))
    my_list.add_in_tail(Node(30))

    my_list.clean()

    assert my_list.head is None
    assert my_list.tail is None


def test_find_all():
    my_list = LinkedList()

    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(20))
    my_list.add_in_tail(Node(30))
    my_list.add_in_tail(Node(20))
    my_list.add_in_tail(Node(30))
    
    nodes = my_list.find_all(20)
    assert len(nodes) == 2
    assert nodes[0].value == 20
    assert nodes[1].value == 20


def test_len():
    my_list = LinkedList()

    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(20))
    my_list.add_in_tail(Node(30))
    my_list.add_in_tail(Node(20))
    my_list.add_in_tail(Node(30))
    
    assert my_list.len() == 5


def test_insert():
    my_list = LinkedList()

    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(20))
    my_list.add_in_tail(Node(30))

    new_node_1 = Node(15)
    new_node_2 = Node(25)
    new_node_3 = Node(5)

    after_node_1 = my_list.head
    my_list.insert(after_node_1, new_node_1)

    after_node_2 = my_list.head.next.next
    my_list.insert(after_node_2, new_node_2)

    after_node_3 = None
    my_list.insert(after_node_3, new_node_3)

    assert my_list.return_all_nodes() == [5, 10, 15, 20, 25, 30]
