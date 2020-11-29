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




