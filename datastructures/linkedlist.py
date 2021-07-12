class Node:
  def __init__(self, data):
    self.data = data
    self.next_element = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def insert_at_head(self, data):
        node = Node(data)

        node.next_element = self.head
        self.head = node

        return self.head

    def insert_at_tail(self, data):
        if self.is_empty():
            self.insert_at_head(data)
        else:
            node = Node(data)
            temp = self.head

            while temp.next_element:
                temp = temp.next_element
                print("print", temp.next_element)
            temp.next_element = node

    def insert_at_k(self, k, data):
        node = Node(data)
        temp = self.head
        count = 0

        while temp.next_element and count < k - 1:
            temp = temp.next_element
            count += 1
        node.next_element = temp.next_element
        temp.next_element = node

    def search(self, value):
        temp = self.head

        while temp.next_element:
            if temp.data == value:
                return "value", value
            temp = temp.next_element

        return "Value does not exist"

    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.data)
            printval = printval.next_element


lst = LinkedList()  # Linked List created
print(lst.is_empty())
print(lst.insert_at_head(5))
print(lst.is_empty())
print(lst.get_head())
print(lst.insert_at_tail(20))
print(lst.insert_at_tail(100000))
print(lst.insert_at_head(5))
print(lst.insert_at_head(5))
print(lst.insert_at_k(1, 100))
print(lst.search(20))
print(lst.listprint())


# Alternate 
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        
    def print_nodes(self):
        last_node = self.head
        
        while last_node:
            print(last_node.data)
            last_node = last_node.next
    
    def insert(self, data):
        node = Node(data)
        
        if self.head == None:
            self.head = node
            return
            
        last_node = self.head
        
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = node
        
    def prepend(self, data):
        node = Node(data)
        
        node.next = self.head
        self.head = node
        
    def insert_at_loc(self, prev_node, data):
        node = Node(data)
        
        if not prev_node:
            return None
        
        node.next = prev_node.next
        prev_node.next = node
        
        
    def removedup(self):
    # Write your code here.
        last_node = self.head
        
        while last_node.next:
            distinctnode = last_node.next
            while distinctnode is not None and distinctnode.data == last_node.data:
                distinctnode = distinctnode.next
                
            last_node.next = distinctnode
            last_node = distinctnode




