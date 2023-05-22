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
        
    assert my_list.return_string_all_nodes() == '5, 10, 15, 20, 25, 30'


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
        
      
def test_clean():
    my_list = LinkedList()

    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(20))
    my_list.add_in_tail(Node(30))
    my_list.add_in_tail(Node(20))
    my_list.add_in_tail(Node(30))
    
    my_list.clean()
    
    assert my_list.head is None
           
      
def test_length():
    my_list = LinkedList()

    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(20))
    my_list.add_in_tail(Node(30))
    my_list.add_in_tail(Node(20))
    my_list.add_in_tail(Node(30))
    
    assert my_list.len() == 5 


def test_delete():
    my_list = LinkedList()

    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(20))
    my_list.add_in_tail(Node(30))
    my_list.add_in_tail(Node(20))
    my_list.add_in_tail(Node(30))
    
    my_list.delete(10)
    
    assert my_list.return_string_all_nodes() == '20, 30, 20, 30'
    
    my_list.delete(20, all=True)
    
    assert my_list.return_string_all_nodes() == '30, 30'
    
    
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
