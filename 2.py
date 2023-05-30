from typing import Optional, List


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val: int) -> Optional[Node]:
        if self.is_empty():
            return None
        current = self.head
        while current is not None:
            if current.value == val:
                return current
            current = current.next
        return None
    
    def delete(self, value: int, all=False):
        if self.is_empty():
            return
        current = self.head
        while current is not None:
            if current.value == value:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                    
                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                if not all:
                    return
                
            current = current.next
             
    def insert(self, afterNode: Optional[Node], newNode: Optional[Node]):
        if afterNode is None:
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            else:
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
                
        else:
            newNode.next = afterNode.next
            newNode.prev = afterNode
            if afterNode.next is not None:
                afterNode.next.prev = newNode
            afterNode.next = newNode
            
    def return_all_nodes(self) -> List[int]:
        nodes = []
        node = self.head
        while node is not None:
            nodes.append(node.value)
            node = node.next
        return nodes
    
    def clean(self):
        self.head = None
        self.tail = None
        
    def is_empty(self) -> bool:
        return self.head is None
    
    def len(self) -> int:
        count = 0
        if self.is_empty():
            return count
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
    
    def add_in_head(self, new_node: Node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None
            
    def find_all(self, val: int) -> List[Node]:
        nodes = []
        if self.is_empty():
            return nodes 
        current = self.head

        while current is not None:
            if current.value == val:
                nodes.append(current)
            current = current.next

        return nodes            
                
                
def test_find():
    my_list = LinkedList2()
    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(20))
    my_list.add_in_tail(Node(30))
    my_list.add_in_tail(Node(40))
    
    node = my_list.find(30)
    assert node.value == 30
    
    
def test_delete():
    my_list = LinkedList2()
    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(20))
    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(10))
    my_list.delete(10, all=True)

    node = my_list.find(10)
    assert node == None
    
    
def test_insert():
    my_list = LinkedList2()
    node = Node(10)
    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(20))
    my_list.add_in_tail(node)
    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(10))
    
    my_list.insert(node, Node(100))
    
    assert my_list.return_all_nodes() == [10, 20, 10, 100, 10, 10]
    
    
def test_insert_when_none_node():
    my_list = LinkedList2()
    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(20))
    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(10))
    
    my_list.insert(None, Node(100))
    assert my_list.return_all_nodes() == [10, 20, 10, 10, 100]
    
    
def test_insert_when_none_node_and_empty_list():
    my_list = LinkedList2()
    
    my_list.insert(None, Node(100))
    assert my_list.return_all_nodes() == [100]
    

def test_clean():
    my_list = LinkedList2()
    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(20))
    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(10))
    
    my_list.clean()
    assert my_list.head == None
    assert my_list.tail == None
    
    
def test_len():
    my_list = LinkedList2()
    assert my_list.len() == 0
    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(20))
    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(10))
    
    assert my_list.len() == 4
    

def test_add_in_head():
    my_list = LinkedList2()
    my_list.add_in_head(Node(0))
    assert my_list.return_all_nodes() == [0]
    
    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(20))
    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(10))
    
    my_list.add_in_head(Node(100))
    
    assert my_list.return_all_nodes() == [100, 0, 10, 20, 10, 10]
    
    
def test_find_all():
    my_list = LinkedList2()
    my_list.add_in_head(Node(0))
    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(20))
    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(10))
    
    nodes = my_list.find_all(10)
    assert nodes[0].value == 10
    assert nodes[1].value == 10
    assert nodes[2].value == 10

    