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
        while node != None:
            print(node.value)
            node = node.next

    def return_string_all_nodes(self):
        if self.is_empty():
            return ''
        node = self.head
        node_string = ''
        while node != None:
            if node != self.head:
                node_string += ', '
            node_string += str(node.value)
            node = node.next
        return node_string    

    def is_empty(self):
        return self.head is None        

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        if self.is_empty():
            return []
        nodes = []
        current = self.head
        while current is not None:
            if current.value == val:
                nodes.append(current)
            current = current.next
        return nodes

    def delete(self, val, all=False):
        if self.is_empty():
            return
        while self.head and self.head.value == val:
            if not all:
                self.head = self.head.next
                return
            else:
                self.head = self.head.next
        current = self.head
        while current and current.next:
            if current.next.value == val:
                if not all:
                    current.next = current.next.next
                    return
                else:
                    current.next = current.next.next
            else:
                current = current.next

    def clean(self):
        if self.is_empty():
            return 
        self.head = None

    def len(self):
        if self.is_empty():
            return 0
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count        

    def insert(self, afterNode, newNode):
        if self.is_empty():
            return
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            return
        newNode.next = afterNode.next
        afterNode.next = newNode

def sum_linked_lists(list1, list2):
    if list1.len() != list2.len():
        return 

    result_list = LinkedList()
    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        sum_value = current1.value + current2.value
        result_list.add_in_tail(Node(sum_value))
        current1 = current1.next
        current2 = current2.next

    return result_list
